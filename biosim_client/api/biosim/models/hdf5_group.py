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

from biosim_client.api.biosim.models.hdf5_attribute import HDF5Attribute
from biosim_client.api.biosim.models.hdf5_dataset import HDF5Dataset


class HDF5Group(BaseModel):
    """
    HDF5Group
    """

    name: StrictStr
    attributes: List[HDF5Attribute]
    datasets: List[HDF5Dataset]
    __properties: ClassVar[List[str]] = ["name", "attributes", "datasets"]

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
        """Create an instance of HDF5Group from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item_attributes in self.attributes:
                if _item_attributes:
                    _items.append(_item_attributes.to_dict())
            _dict["attributes"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in datasets (list)
        _items = []
        if self.datasets:
            for _item_datasets in self.datasets:
                if _item_datasets:
                    _items.append(_item_datasets.to_dict())
            _dict["datasets"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HDF5Group from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "attributes": [HDF5Attribute.from_dict(_item) for _item in obj["attributes"]]
            if obj.get("attributes") is not None
            else None,
            "datasets": [HDF5Dataset.from_dict(_item) for _item in obj["datasets"]]
            if obj.get("datasets") is not None
            else None,
        })
        return _obj
