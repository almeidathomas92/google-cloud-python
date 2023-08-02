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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
from google.protobuf import empty_pb2  # type: ignore

from google.cloud.iap_v1 import gapic_version as package_version
from google.cloud.iap_v1.types import service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


class IdentityAwareProxyOAuthServiceTransport(abc.ABC):
    """Abstract transport class for IdentityAwareProxyOAuthService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "iap.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )
        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_brands: gapic_v1.method.wrap_method(
                self.list_brands,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_brand: gapic_v1.method.wrap_method(
                self.create_brand,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_brand: gapic_v1.method.wrap_method(
                self.get_brand,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_identity_aware_proxy_client: gapic_v1.method.wrap_method(
                self.create_identity_aware_proxy_client,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_identity_aware_proxy_clients: gapic_v1.method.wrap_method(
                self.list_identity_aware_proxy_clients,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_identity_aware_proxy_client: gapic_v1.method.wrap_method(
                self.get_identity_aware_proxy_client,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_identity_aware_proxy_client_secret: gapic_v1.method.wrap_method(
                self.reset_identity_aware_proxy_client_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_identity_aware_proxy_client: gapic_v1.method.wrap_method(
                self.delete_identity_aware_proxy_client,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def list_brands(
        self,
    ) -> Callable[
        [service.ListBrandsRequest],
        Union[service.ListBrandsResponse, Awaitable[service.ListBrandsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def create_brand(
        self,
    ) -> Callable[
        [service.CreateBrandRequest], Union[service.Brand, Awaitable[service.Brand]]
    ]:
        raise NotImplementedError()

    @property
    def get_brand(
        self,
    ) -> Callable[
        [service.GetBrandRequest], Union[service.Brand, Awaitable[service.Brand]]
    ]:
        raise NotImplementedError()

    @property
    def create_identity_aware_proxy_client(
        self,
    ) -> Callable[
        [service.CreateIdentityAwareProxyClientRequest],
        Union[
            service.IdentityAwareProxyClient,
            Awaitable[service.IdentityAwareProxyClient],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_identity_aware_proxy_clients(
        self,
    ) -> Callable[
        [service.ListIdentityAwareProxyClientsRequest],
        Union[
            service.ListIdentityAwareProxyClientsResponse,
            Awaitable[service.ListIdentityAwareProxyClientsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_identity_aware_proxy_client(
        self,
    ) -> Callable[
        [service.GetIdentityAwareProxyClientRequest],
        Union[
            service.IdentityAwareProxyClient,
            Awaitable[service.IdentityAwareProxyClient],
        ],
    ]:
        raise NotImplementedError()

    @property
    def reset_identity_aware_proxy_client_secret(
        self,
    ) -> Callable[
        [service.ResetIdentityAwareProxyClientSecretRequest],
        Union[
            service.IdentityAwareProxyClient,
            Awaitable[service.IdentityAwareProxyClient],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_identity_aware_proxy_client(
        self,
    ) -> Callable[
        [service.DeleteIdentityAwareProxyClientRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("IdentityAwareProxyOAuthServiceTransport",)