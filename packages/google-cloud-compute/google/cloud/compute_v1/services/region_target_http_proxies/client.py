# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from collections import OrderedDict
import functools
import os
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import extended_operation, gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.compute_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import extended_operation  # type: ignore

from google.cloud.compute_v1.services.region_target_http_proxies import pagers
from google.cloud.compute_v1.types import compute

from .transports.base import DEFAULT_CLIENT_INFO, RegionTargetHttpProxiesTransport
from .transports.rest import RegionTargetHttpProxiesRestTransport


class RegionTargetHttpProxiesClientMeta(type):
    """Metaclass for the RegionTargetHttpProxies client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[RegionTargetHttpProxiesTransport]]
    _transport_registry["rest"] = RegionTargetHttpProxiesRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[RegionTargetHttpProxiesTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class RegionTargetHttpProxiesClient(metaclass=RegionTargetHttpProxiesClientMeta):
    """The RegionTargetHttpProxies API."""

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "compute.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RegionTargetHttpProxiesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RegionTargetHttpProxiesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> RegionTargetHttpProxiesTransport:
        """Returns the transport used by the client instance.

        Returns:
            RegionTargetHttpProxiesTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[Union[str, RegionTargetHttpProxiesTransport]] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the region target http proxies client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, RegionTargetHttpProxiesTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
                NOTE: "rest" transport functionality is currently in a
                beta state (preview). We welcome your feedback via an
                issue in this library's source repository.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        client_options = cast(client_options_lib.ClientOptions, client_options)

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(
            client_options
        )

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, RegionTargetHttpProxiesTransport):
            # transport is a RegionTargetHttpProxiesTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=client_options.api_audience,
            )

    def delete_unary(
        self,
        request: Optional[
            Union[compute.DeleteRegionTargetHttpProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        region: Optional[str] = None,
        target_http_proxy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Deletes the specified TargetHttpProxy resource.

        Args:
            request (Union[google.cloud.compute_v1.types.DeleteRegionTargetHttpProxyRequest, dict]):
                The request object. A request message for
                RegionTargetHttpProxies.Delete. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (str):
                Name of the region scoping this
                request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_http_proxy (str):
                Name of the TargetHttpProxy resource
                to delete.

                This corresponds to the ``target_http_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, region, target_http_proxy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.DeleteRegionTargetHttpProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.DeleteRegionTargetHttpProxyRequest):
            request = compute.DeleteRegionTargetHttpProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if region is not None:
                request.region = region
            if target_http_proxy is not None:
                request.target_http_proxy = target_http_proxy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("region", request.region),
                    ("target_http_proxy", request.target_http_proxy),
                )
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete(
        self,
        request: Optional[
            Union[compute.DeleteRegionTargetHttpProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        region: Optional[str] = None,
        target_http_proxy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Deletes the specified TargetHttpProxy resource.

        Args:
            request (Union[google.cloud.compute_v1.types.DeleteRegionTargetHttpProxyRequest, dict]):
                The request object. A request message for
                RegionTargetHttpProxies.Delete. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (str):
                Name of the region scoping this
                request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_http_proxy (str):
                Name of the TargetHttpProxy resource
                to delete.

                This corresponds to the ``target_http_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, region, target_http_proxy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.DeleteRegionTargetHttpProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.DeleteRegionTargetHttpProxyRequest):
            request = compute.DeleteRegionTargetHttpProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if region is not None:
                request.region = region
            if target_http_proxy is not None:
                request.target_http_proxy = target_http_proxy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("region", request.region),
                    ("target_http_proxy", request.target_http_proxy),
                )
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._region_operations_client
        operation_request = compute.GetRegionOperationRequest()
        operation_request.project = request.project
        operation_request.region = request.region
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def get(
        self,
        request: Optional[Union[compute.GetRegionTargetHttpProxyRequest, dict]] = None,
        *,
        project: Optional[str] = None,
        region: Optional[str] = None,
        target_http_proxy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.TargetHttpProxy:
        r"""Returns the specified TargetHttpProxy resource in the
        specified region. Gets a list of available target HTTP
        proxies by making a list() request.

        Args:
            request (Union[google.cloud.compute_v1.types.GetRegionTargetHttpProxyRequest, dict]):
                The request object. A request message for
                RegionTargetHttpProxies.Get. See the method description
                for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (str):
                Name of the region scoping this
                request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_http_proxy (str):
                Name of the TargetHttpProxy resource
                to return.

                This corresponds to the ``target_http_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.compute_v1.types.TargetHttpProxy:
                Represents a Target HTTP Proxy resource. Google Compute
                Engine has two Target HTTP Proxy resources: \*
                [Global](/compute/docs/reference/rest/v1/targetHttpProxies)
                \*
                [Regional](/compute/docs/reference/rest/v1/regionTargetHttpProxies)
                A target HTTP proxy is a component of GCP HTTP load
                balancers. \* targetHttpProxies are used by external
                HTTP load balancers and Traffic Director. \*
                regionTargetHttpProxies are used by internal HTTP load
                balancers. Forwarding rules reference a target HTTP
                proxy, and the target proxy then references a URL map.
                For more information, read Using Target Proxies and
                Forwarding rule concepts.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, region, target_http_proxy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.GetRegionTargetHttpProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.GetRegionTargetHttpProxyRequest):
            request = compute.GetRegionTargetHttpProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if region is not None:
                request.region = region
            if target_http_proxy is not None:
                request.target_http_proxy = target_http_proxy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("region", request.region),
                    ("target_http_proxy", request.target_http_proxy),
                )
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def insert_unary(
        self,
        request: Optional[
            Union[compute.InsertRegionTargetHttpProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        region: Optional[str] = None,
        target_http_proxy_resource: Optional[compute.TargetHttpProxy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Creates a TargetHttpProxy resource in the specified
        project and region using the data included in the
        request.

        Args:
            request (Union[google.cloud.compute_v1.types.InsertRegionTargetHttpProxyRequest, dict]):
                The request object. A request message for
                RegionTargetHttpProxies.Insert. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (str):
                Name of the region scoping this
                request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_http_proxy_resource (google.cloud.compute_v1.types.TargetHttpProxy):
                The body resource for this request
                This corresponds to the ``target_http_proxy_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, region, target_http_proxy_resource])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.InsertRegionTargetHttpProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.InsertRegionTargetHttpProxyRequest):
            request = compute.InsertRegionTargetHttpProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if region is not None:
                request.region = region
            if target_http_proxy_resource is not None:
                request.target_http_proxy_resource = target_http_proxy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.insert]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("region", request.region),
                )
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def insert(
        self,
        request: Optional[
            Union[compute.InsertRegionTargetHttpProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        region: Optional[str] = None,
        target_http_proxy_resource: Optional[compute.TargetHttpProxy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Creates a TargetHttpProxy resource in the specified
        project and region using the data included in the
        request.

        Args:
            request (Union[google.cloud.compute_v1.types.InsertRegionTargetHttpProxyRequest, dict]):
                The request object. A request message for
                RegionTargetHttpProxies.Insert. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (str):
                Name of the region scoping this
                request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_http_proxy_resource (google.cloud.compute_v1.types.TargetHttpProxy):
                The body resource for this request
                This corresponds to the ``target_http_proxy_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, region, target_http_proxy_resource])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.InsertRegionTargetHttpProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.InsertRegionTargetHttpProxyRequest):
            request = compute.InsertRegionTargetHttpProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if region is not None:
                request.region = region
            if target_http_proxy_resource is not None:
                request.target_http_proxy_resource = target_http_proxy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.insert]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("region", request.region),
                )
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._region_operations_client
        operation_request = compute.GetRegionOperationRequest()
        operation_request.project = request.project
        operation_request.region = request.region
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def list(
        self,
        request: Optional[
            Union[compute.ListRegionTargetHttpProxiesRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        region: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPager:
        r"""Retrieves the list of TargetHttpProxy resources
        available to the specified project in the specified
        region.

        Args:
            request (Union[google.cloud.compute_v1.types.ListRegionTargetHttpProxiesRequest, dict]):
                The request object. A request message for
                RegionTargetHttpProxies.List. See the method description
                for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (str):
                Name of the region scoping this
                request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.compute_v1.services.region_target_http_proxies.pagers.ListPager:
                A list of TargetHttpProxy resources.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, region])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.ListRegionTargetHttpProxiesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.ListRegionTargetHttpProxiesRequest):
            request = compute.ListRegionTargetHttpProxiesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if region is not None:
                request.region = region

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("region", request.region),
                )
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_url_map_unary(
        self,
        request: Optional[
            Union[compute.SetUrlMapRegionTargetHttpProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        region: Optional[str] = None,
        target_http_proxy: Optional[str] = None,
        url_map_reference_resource: Optional[compute.UrlMapReference] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Changes the URL map for TargetHttpProxy.

        Args:
            request (Union[google.cloud.compute_v1.types.SetUrlMapRegionTargetHttpProxyRequest, dict]):
                The request object. A request message for
                RegionTargetHttpProxies.SetUrlMap. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (str):
                Name of the region scoping this
                request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_http_proxy (str):
                Name of the TargetHttpProxy to set a
                URL map for.

                This corresponds to the ``target_http_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            url_map_reference_resource (google.cloud.compute_v1.types.UrlMapReference):
                The body resource for this request
                This corresponds to the ``url_map_reference_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [project, region, target_http_proxy, url_map_reference_resource]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetUrlMapRegionTargetHttpProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetUrlMapRegionTargetHttpProxyRequest):
            request = compute.SetUrlMapRegionTargetHttpProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if region is not None:
                request.region = region
            if target_http_proxy is not None:
                request.target_http_proxy = target_http_proxy
            if url_map_reference_resource is not None:
                request.url_map_reference_resource = url_map_reference_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_url_map]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("region", request.region),
                    ("target_http_proxy", request.target_http_proxy),
                )
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_url_map(
        self,
        request: Optional[
            Union[compute.SetUrlMapRegionTargetHttpProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        region: Optional[str] = None,
        target_http_proxy: Optional[str] = None,
        url_map_reference_resource: Optional[compute.UrlMapReference] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Changes the URL map for TargetHttpProxy.

        Args:
            request (Union[google.cloud.compute_v1.types.SetUrlMapRegionTargetHttpProxyRequest, dict]):
                The request object. A request message for
                RegionTargetHttpProxies.SetUrlMap. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (str):
                Name of the region scoping this
                request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_http_proxy (str):
                Name of the TargetHttpProxy to set a
                URL map for.

                This corresponds to the ``target_http_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            url_map_reference_resource (google.cloud.compute_v1.types.UrlMapReference):
                The body resource for this request
                This corresponds to the ``url_map_reference_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [project, region, target_http_proxy, url_map_reference_resource]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetUrlMapRegionTargetHttpProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetUrlMapRegionTargetHttpProxyRequest):
            request = compute.SetUrlMapRegionTargetHttpProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if region is not None:
                request.region = region
            if target_http_proxy is not None:
                request.target_http_proxy = target_http_proxy
            if url_map_reference_resource is not None:
                request.url_map_reference_resource = url_map_reference_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_url_map]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("region", request.region),
                    ("target_http_proxy", request.target_http_proxy),
                )
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._region_operations_client
        operation_request = compute.GetRegionOperationRequest()
        operation_request.project = request.project
        operation_request.region = request.region
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("RegionTargetHttpProxiesClient",)