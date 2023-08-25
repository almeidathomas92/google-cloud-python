# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.config_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.config import ConfigAsyncClient, ConfigClient
from .types.config import (
    ApplyResults,
    CreateDeploymentRequest,
    DeleteDeploymentRequest,
    DeleteStatefileRequest,
    Deployment,
    DeploymentOperationMetadata,
    ExportDeploymentStatefileRequest,
    ExportLockInfoRequest,
    ExportRevisionStatefileRequest,
    GetDeploymentRequest,
    GetResourceRequest,
    GetRevisionRequest,
    GitSource,
    ImportStatefileRequest,
    ListDeploymentsRequest,
    ListDeploymentsResponse,
    ListResourcesRequest,
    ListResourcesResponse,
    ListRevisionsRequest,
    ListRevisionsResponse,
    LockDeploymentRequest,
    LockInfo,
    OperationMetadata,
    Resource,
    ResourceCAIInfo,
    ResourceTerraformInfo,
    Revision,
    Statefile,
    TerraformBlueprint,
    TerraformError,
    TerraformOutput,
    TerraformVariable,
    UnlockDeploymentRequest,
    UpdateDeploymentRequest,
)

__all__ = (
    "ConfigAsyncClient",
    "ApplyResults",
    "ConfigClient",
    "CreateDeploymentRequest",
    "DeleteDeploymentRequest",
    "DeleteStatefileRequest",
    "Deployment",
    "DeploymentOperationMetadata",
    "ExportDeploymentStatefileRequest",
    "ExportLockInfoRequest",
    "ExportRevisionStatefileRequest",
    "GetDeploymentRequest",
    "GetResourceRequest",
    "GetRevisionRequest",
    "GitSource",
    "ImportStatefileRequest",
    "ListDeploymentsRequest",
    "ListDeploymentsResponse",
    "ListResourcesRequest",
    "ListResourcesResponse",
    "ListRevisionsRequest",
    "ListRevisionsResponse",
    "LockDeploymentRequest",
    "LockInfo",
    "OperationMetadata",
    "Resource",
    "ResourceCAIInfo",
    "ResourceTerraformInfo",
    "Revision",
    "Statefile",
    "TerraformBlueprint",
    "TerraformError",
    "TerraformOutput",
    "TerraformVariable",
    "UnlockDeploymentRequest",
    "UpdateDeploymentRequest",
)
