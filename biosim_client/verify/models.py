from io import BytesIO
from typing import TypeAlias
from zipfile import ZIP_DEFLATED, ZipFile

import fitz  # type: ignore
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib3
from IPython.display import Markdown, display
from PIL.Image import Image
from PIL.PngImagePlugin import PngImageFile

from biosim_client.api.biosim.models.biosim_simulation_run import BiosimSimulationRun
from biosim_client.api.biosim.models.biosimulator_version import BiosimulatorVersion
from biosim_client.api.biosim.models.comparison_statistics import ComparisonStatistics
from biosim_client.api.biosim.models.generate_statistics_activity_output import GenerateStatisticsActivityOutput
from biosim_client.api.biosim.models.hdf5_attribute import HDF5Attribute as BiosimHDF5Attribute
from biosim_client.api.biosim.models.hdf5_file import HDF5File as BiosimHDF5File
from biosim_client.api.biosim.models.simulation_run_info import SimulationRunInfo
from biosim_client.api.biosim.models.verify_workflow_output import VerifyWorkflowOutput
from biosim_client.api.simdata.api.default_api import DefaultApi as SimdataDefaultApi
from biosim_client.api.simdata.api_client import ApiClient as SimdataApiClient
from biosim_client.api.simdata.models.hdf5_attribute import HDF5Attribute as SimDataHDF5Attribute
from biosim_client.api.simdata.models.hdf5_file import HDF5File as SimDataHDF5File
from biosim_client.simdata.sim_data import SimData
from biosim_client.simdata.simdata_client import simdata_configuration

NDArray3D: TypeAlias = np.ndarray[tuple[int, int, int], np.dtype[np.float64]]


class DatasetComparison:
    dataset_name: str
    var_names: list[str]
    run_ids: list[str]
    dataset_score: NDArray3D  # shape=(len(var_names), len(run_ids), len(run_ids))

    def __init__(
        self, dataset_name: str, var_names: list[str], run_ids: list[str], stats_list: list[list[ComparisonStatistics]]
    ) -> None:
        self.dataset_name = dataset_name
        self.var_names = var_names
        self.run_ids = run_ids
        self.dataset_score = self.parse_stats(stats_list=stats_list)

    def parse_stats(self, stats_list: list[list[ComparisonStatistics]]) -> NDArray3D:
        shape: tuple[int, int, int] = (len(self.var_names), len(self.run_ids), len(self.run_ids))
        array: NDArray3D = np.full(dtype=np.float64, shape=shape, fill_value=np.inf)
        for i in range(len(self.run_ids)):
            for j in range(len(self.run_ids)):
                stats: ComparisonStatistics = stats_list[i][j]
                if stats is not None and stats.score is not None:
                    array[:, i, j] = [float(score) for score in stats.score]
        return array

    def __str__(self) -> str:
        return f"DatasetComparison(dataset_name={self.dataset_name}, var_names={self.var_names}, run_ids={self.run_ids}, score={self.dataset_score})"


class VerifyResults:
    run_verify_results: VerifyWorkflowOutput
    workflow_results: GenerateStatisticsActivityOutput

    def __init__(self, run_verify_results: VerifyWorkflowOutput) -> None:
        self.run_verify_results = run_verify_results
        if self.run_verify_results.workflow_results is None:
            raise ValueError("No workflow results")
        self.workflow_results = self.run_verify_results.workflow_results

    def get_simdata(self) -> list[SimData]:
        sim_data_list: list[SimData] = []
        with SimdataApiClient(simdata_configuration) as simdata_api_client:
            api_instance = SimdataDefaultApi(simdata_api_client)
            for sim_run_info in self.workflow_results.sims_run_info:
                simdata_hdf5_file: SimDataHDF5File = api_instance.get_metadata(sim_run_info.biosim_sim_run.id)
                sim_data_list.append(
                    SimData(
                        run_id=sim_run_info.biosim_sim_run.id,
                        hdf5_file=simdata_hdf5_file,
                        simulator_version=sim_run_info.biosim_sim_run.simulator_version,
                    )
                )
        return sim_data_list

    @property
    def simulator_versions(self) -> list[BiosimulatorVersion]:
        return [sim_ver.biosim_sim_run.simulator_version for sim_ver in self.workflow_results.sims_run_info]

    @property
    def simulator_version_names(self) -> list[str]:
        if self.simulator_versions is None:
            return []
        return [f"{sim_ver.id}:{sim_ver.version}" for sim_ver in self.simulator_versions]

    @property
    def dataset_names(self) -> list[str]:
        return list(self.workflow_results.comparison_statistics.keys())

    def get_dataset_comparison(self, dataset_name: str) -> DatasetComparison | None:
        first_sim_run_info: SimulationRunInfo | None = None
        if self.workflow_results.sims_run_info is not None:
            for sim_run_info in self.workflow_results.sims_run_info:
                if sim_run_info is not None:
                    first_sim_run_info = sim_run_info
                    break
        if first_sim_run_info is None:
            return None  # no data to compare
        for stat_dataset_name, stats_list in self.workflow_results.comparison_statistics.items():
            if stat_dataset_name == dataset_name:
                var_names: list[str] = self.get_var_names(dataset_name)
                return DatasetComparison(
                    dataset_name=dataset_name, var_names=var_names, run_ids=self.run_ids, stats_list=stats_list
                )
        return None

    @property
    def run_ids(self) -> list[str]:
        return [sim_run_info.biosim_sim_run.id for sim_run_info in self.workflow_results.sims_run_info]

    @property
    def runs(self) -> list[BiosimSimulationRun]:
        return [sim_run_info.biosim_sim_run for sim_run_info in self.workflow_results.sims_run_info]

    def get_var_names(self, dataset_name: str) -> list[str]:
        if len(self.workflow_results.sims_run_info) == 0:
            return []

        # get var names from HDF5 labels attribute of dataset from first sim run
        hdf5_file: BiosimHDF5File = self.workflow_results.sims_run_info[0].hdf5_file
        attr = _extract_dataset_attr(dataset_name=dataset_name, hdf5_file=hdf5_file, attr_key="sedmlDataSetLabels")
        if attr is None:
            return []
        else:
            value: list[str] = attr.model_dump()["value"]["actual_instance"]
            return value

    def show_dataset_heatmaps(self) -> None:
        sim_version_names = self.simulator_version_names
        ds_names = self.dataset_names
        # Assuming 'score' and 'sim_version_names' are defined from the previous code

        fig, axes = plt.subplots(len(ds_names), 1, figsize=(10, 5 * len(ds_names)))  # Adjust figsize as needed

        if len(ds_names) == 1:
            axes = [axes]

        for i, dataset_name in enumerate(ds_names):
            dataset_comparison: DatasetComparison | None = self.get_dataset_comparison(dataset_name=dataset_name)
            if dataset_comparison is None:
                raise ValueError(f"Dataset comparison not found for dataset: {dataset_name}")
            score: NDArray3D = dataset_comparison.dataset_score
            max_scores = np.max(score, axis=0)  # axis 0 to get max score across variables.

            im = axes[i].imshow(max_scores, cmap="viridis", interpolation="nearest")
            axes[i].set_xticks(np.arange(len(sim_version_names)))
            axes[i].set_yticks(np.arange(len(sim_version_names)))

            # Add solver names as labels
            axes[i].set_xticklabels(sim_version_names, rotation=45, ha="right", rotation_mode="anchor")
            axes[i].set_yticklabels(sim_version_names)
            axes[i].set_title(f"{dataset_name}")

            # Loop over data dimensions and create text annotations.
            for x in range(len(sim_version_names)):
                for y in range(len(sim_version_names)):
                    axes[i].text(x, y, f"{max_scores[x, y]:.8f}", ha="center", va="center", color="r", fontsize=8)

            fig.colorbar(im, ax=axes[i])

        plt.tight_layout()  # Adjust layout to prevent overlapping elements
        plt.show()

    def _get_max_score(self, run_id1: str, run_id2: str) -> float:
        for sim_run_info in self.workflow_results.sims_run_info:
            if sim_run_info is not None:
                break
        index_1 = self.run_ids.index(run_id1)
        index_2 = self.run_ids.index(run_id2)
        max_score = 0.0
        for dataset_name in self.dataset_names:
            dataset_comparison: DatasetComparison | None = self.get_dataset_comparison(dataset_name)
            if dataset_comparison is None:
                return np.inf
            score_i_j = dataset_comparison.dataset_score[:, index_1, index_2]
            score_j_i = dataset_comparison.dataset_score[:, index_2, index_1]
            max_score = max(max_score, np.max(score_i_j), np.max(score_j_i))
        return max_score

    def get_run_comparison_clusters(self) -> list[tuple[list[BiosimSimulationRun], float, float]]:
        for sim_run_info in self.workflow_results.comparison_statistics:
            if sim_run_info is not None:
                break
        matched_run_groups: list[tuple[list[BiosimSimulationRun], float, float]] = []
        unmatched_runs = self.runs.copy()

        while len(unmatched_runs) > 0:
            # create new match group where all scores are less than 1.0
            run = unmatched_runs.pop(0)
            matched_group = [run]
            max_score = 0.0
            for other_run in self.runs:
                if run.id == other_run.id or other_run not in unmatched_runs:
                    continue
                score = self._get_max_score(run.id, other_run.id)
                if score < 1.0:
                    matched_group.append(other_run)
                    unmatched_runs.remove(other_run)
                    max_score = max(max_score, score)
            # compute min score for all members of matched_group to all runs
            min_score = np.inf
            for i in range(len(matched_group)):
                for j in range(i + 1, len(self.runs)):
                    if matched_group[i].id != self.runs[j].id:
                        min_score = min(min_score, self._get_max_score(matched_group[i].id, self.runs[j].id))
            matched_run_groups.append((matched_group, min_score, max_score))

        return matched_run_groups

    def show_report(self) -> None:
        # display as markdown for jupyter notebook
        markdown_report = self._create_markdown_report()
        display(Markdown(markdown_report))  # type: ignore

    def _create_markdown_report(self) -> str:
        simulator_markdown = ""
        run_link_map: dict[str, str] = {
            run.id: f"[{run.simulator_version.id}:{run.simulator_version.version}](https://biosimulations.org/runs/{run.id})"
            for run in self.runs
        }
        run_comparison_clusters = self.get_run_comparison_clusters()
        for run_group, min_score, max_score in run_comparison_clusters:
            if len(run_group) > 1:
                run_group_links = ", ".join([run_link_map[run.id] for run in run_group])
                simulator_markdown += f"- Group [{run_group_links}] matched (max score {max_score})\n"
            else:
                simulator_markdown += f"- no match for {run_link_map[run_group[0].id]} (closest score {min_score})\n"
        return simulator_markdown

    def show_saved_plots(self, max_columns: int = 3, width_in: float = 10) -> None:
        images: list[Image] = []
        image_run_ids = []
        image_not_found_run_ids = []
        sim_version_names = self.simulator_version_names
        http = urllib3.PoolManager()
        for run_id in self.run_ids:
            pdf_images: list[PngImageFile] = self._retrieve_pdf_as_image(run_id=run_id, http=http)
            if len(pdf_images) == 0:
                image_not_found_run_ids.append(run_id)
            elif len(pdf_images) == 1:
                images.append(pdf_images[0])
                image_run_ids.append(run_id)
            else:
                # concatenate all images in pdf_images into a single image
                width = max([image.width for image in pdf_images])
                height = sum([image.height for image in pdf_images])
                new_image = PIL.Image.new("RGB", (width, height))
                y_offset = 0
                for image in pdf_images:
                    new_image.paste(image, (0, y_offset))
                    y_offset += image.height
                images.append(new_image)
                # images.append(ImageFile(new_image.tobytes("png")))
                image_run_ids.append(run_id)

        if len(images) == 0:
            display(f"no saved plots for runs {image_not_found_run_ids}")  # type: ignore
            return

        # determine number of columns and rows, start with max_columns and reduce to two columns
        # until the number of images is divisible (or almost divisible) by number of columns
        ncols = min(len(images), max_columns)
        while len(images) % ncols != 0 and len(images) % ncols != (ncols - 1) and ncols > 2:
            ncols -= 1
        nrows = len(images) // ncols + 1

        width_pixels = max([image.width for image in images]) * ncols
        height_pixels = max([image.height for image in images]) * nrows
        height_in = width_in * height_pixels / width_pixels
        figsize = (width_in, height_in)
        fig, ax = plt.subplots(ncols=ncols, nrows=nrows, figsize=figsize)
        ax = ax.flatten()
        for i in range(nrows * ncols):
            if i >= len(images):
                ax[i].axis("off")
                ax[i].set_title("")
                ax[i].set_visible(False)
            else:
                ax[i].axis("off")
                ax[i].set_title(f"{sim_version_names[i]}")
                ax[i].imshow(images[i])

        plt.tight_layout()
        plt.show()

    def _retrieve_pdf_as_image(self, run_id: str, http: urllib3.PoolManager) -> list[PngImageFile]:
        pdf_url = f"https://api.biosimulations.org/results/{run_id}/download"
        images: list[PngImageFile] = []
        head_response = http.request("HEAD", pdf_url)
        if head_response.status == 200:
            response = http.request("GET", pdf_url)
            with BytesIO(response.data) as zip_buffer, ZipFile(zip_buffer, "a", ZIP_DEFLATED, False) as zip_file:
                file_names = zip_file.namelist()
                for file_name in file_names:
                    if file_name.endswith(".pdf") and file_name.lower().index("plot") != -1:
                        with zip_file.open(file_name) as pdf_file:
                            content = pdf_file.read()
                            with fitz.open(stream=content, filetype="pdf") as doc:
                                for page in doc:
                                    pix: fitz.Pixmap = page.get_pixmap()
                                    png_content = pix.tobytes("png")
                                    images.append(PIL.Image.open(BytesIO(png_content)))  # type: ignore
        return images


def _extract_dataset_attr(
    dataset_name: str, attr_key: str, hdf5_file: BiosimHDF5File | SimDataHDF5File
) -> BiosimHDF5Attribute | SimDataHDF5Attribute | None:
    for group in hdf5_file.groups:
        for dataset in group.datasets:
            if dataset.name == dataset_name:
                for attr in dataset.attributes:
                    if attr.key == attr_key:
                        return attr
    return None
