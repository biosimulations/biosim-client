"""
biosim-server

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations

import json
from enum import Enum

from typing_extensions import Self


class RunsVerifyWorkflowStatus(str, Enum):
    """
    RunsVerifyWorkflowStatus
    """

    """
    allowed enum values
    """
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    RUN_ID_NOT_FOUND = "RUN_ID_NOT_FOUND"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RunsVerifyWorkflowStatus from a JSON string"""
        return cls(json.loads(json_str))
