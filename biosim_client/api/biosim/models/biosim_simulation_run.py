"""
biosim-server

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, StrictStr
from typing_extensions import Self

from biosim_client.api.biosim.models.biosim_simulation_run_status import BiosimSimulationRunStatus
from biosim_client.api.biosim.models.biosimulator_version import BiosimulatorVersion


class BiosimSimulationRun(BaseModel):
    """
    data returned by api.biosimulations.org/runs/{run_id}
    """

    id: StrictStr
    name: StrictStr
    simulator_version: BiosimulatorVersion
    status: BiosimSimulationRunStatus
    error_message: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "name", "simulator_version", "status", "error_message"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BiosimSimulationRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of simulator_version
        if self.simulator_version:
            _dict["simulator_version"] = self.simulator_version.to_dict()
        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict["error_message"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BiosimSimulationRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "simulator_version": BiosimulatorVersion.from_dict(obj["simulator_version"])
            if obj.get("simulator_version") is not None
            else None,
            "status": obj.get("status"),
            "error_message": obj.get("error_message"),
        })
        return _obj
