# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.servicehealth_v1.types import event_resources


class ListEventsPager:
    """A pager for iterating through ``list_events`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.servicehealth_v1.types.ListEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvents`` requests and continue to iterate
    through the ``events`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.servicehealth_v1.types.ListEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., event_resources.ListEventsResponse],
        request: event_resources.ListEventsRequest,
        response: event_resources.ListEventsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.servicehealth_v1.types.ListEventsRequest):
                The initial request object.
            response (google.cloud.servicehealth_v1.types.ListEventsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = event_resources.ListEventsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[event_resources.ListEventsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[event_resources.Event]:
        for page in self.pages:
            yield from page.events

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEventsAsyncPager:
    """A pager for iterating through ``list_events`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.servicehealth_v1.types.ListEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvents`` requests and continue to iterate
    through the ``events`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.servicehealth_v1.types.ListEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[event_resources.ListEventsResponse]],
        request: event_resources.ListEventsRequest,
        response: event_resources.ListEventsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.servicehealth_v1.types.ListEventsRequest):
                The initial request object.
            response (google.cloud.servicehealth_v1.types.ListEventsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = event_resources.ListEventsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[event_resources.ListEventsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[event_resources.Event]:
        async def async_generator():
            async for page in self.pages:
                for response in page.events:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOrganizationEventsPager:
    """A pager for iterating through ``list_organization_events`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.servicehealth_v1.types.ListOrganizationEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``organization_events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOrganizationEvents`` requests and continue to iterate
    through the ``organization_events`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.servicehealth_v1.types.ListOrganizationEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., event_resources.ListOrganizationEventsResponse],
        request: event_resources.ListOrganizationEventsRequest,
        response: event_resources.ListOrganizationEventsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.servicehealth_v1.types.ListOrganizationEventsRequest):
                The initial request object.
            response (google.cloud.servicehealth_v1.types.ListOrganizationEventsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = event_resources.ListOrganizationEventsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[event_resources.ListOrganizationEventsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[event_resources.OrganizationEvent]:
        for page in self.pages:
            yield from page.organization_events

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOrganizationEventsAsyncPager:
    """A pager for iterating through ``list_organization_events`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.servicehealth_v1.types.ListOrganizationEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``organization_events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOrganizationEvents`` requests and continue to iterate
    through the ``organization_events`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.servicehealth_v1.types.ListOrganizationEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[event_resources.ListOrganizationEventsResponse]
        ],
        request: event_resources.ListOrganizationEventsRequest,
        response: event_resources.ListOrganizationEventsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.servicehealth_v1.types.ListOrganizationEventsRequest):
                The initial request object.
            response (google.cloud.servicehealth_v1.types.ListOrganizationEventsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = event_resources.ListOrganizationEventsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[event_resources.ListOrganizationEventsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[event_resources.OrganizationEvent]:
        async def async_generator():
            async for page in self.pages:
                for response in page.organization_events:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOrganizationImpactsPager:
    """A pager for iterating through ``list_organization_impacts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.servicehealth_v1.types.ListOrganizationImpactsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``organization_impacts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOrganizationImpacts`` requests and continue to iterate
    through the ``organization_impacts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.servicehealth_v1.types.ListOrganizationImpactsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., event_resources.ListOrganizationImpactsResponse],
        request: event_resources.ListOrganizationImpactsRequest,
        response: event_resources.ListOrganizationImpactsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.servicehealth_v1.types.ListOrganizationImpactsRequest):
                The initial request object.
            response (google.cloud.servicehealth_v1.types.ListOrganizationImpactsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = event_resources.ListOrganizationImpactsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[event_resources.ListOrganizationImpactsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[event_resources.OrganizationImpact]:
        for page in self.pages:
            yield from page.organization_impacts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOrganizationImpactsAsyncPager:
    """A pager for iterating through ``list_organization_impacts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.servicehealth_v1.types.ListOrganizationImpactsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``organization_impacts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOrganizationImpacts`` requests and continue to iterate
    through the ``organization_impacts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.servicehealth_v1.types.ListOrganizationImpactsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[event_resources.ListOrganizationImpactsResponse]
        ],
        request: event_resources.ListOrganizationImpactsRequest,
        response: event_resources.ListOrganizationImpactsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.servicehealth_v1.types.ListOrganizationImpactsRequest):
                The initial request object.
            response (google.cloud.servicehealth_v1.types.ListOrganizationImpactsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = event_resources.ListOrganizationImpactsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[event_resources.ListOrganizationImpactsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[event_resources.OrganizationImpact]:
        async def async_generator():
            async for page in self.pages:
                for response in page.organization_impacts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
