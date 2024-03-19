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

from google.cloud.dataplex_v1.types import catalog


class ListEntryTypesPager:
    """A pager for iterating through ``list_entry_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListEntryTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entry_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEntryTypes`` requests and continue to iterate
    through the ``entry_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListEntryTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., catalog.ListEntryTypesResponse],
        request: catalog.ListEntryTypesRequest,
        response: catalog.ListEntryTypesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListEntryTypesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListEntryTypesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.ListEntryTypesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[catalog.ListEntryTypesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[catalog.EntryType]:
        for page in self.pages:
            yield from page.entry_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEntryTypesAsyncPager:
    """A pager for iterating through ``list_entry_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListEntryTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entry_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEntryTypes`` requests and continue to iterate
    through the ``entry_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListEntryTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[catalog.ListEntryTypesResponse]],
        request: catalog.ListEntryTypesRequest,
        response: catalog.ListEntryTypesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListEntryTypesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListEntryTypesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.ListEntryTypesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[catalog.ListEntryTypesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[catalog.EntryType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entry_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAspectTypesPager:
    """A pager for iterating through ``list_aspect_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListAspectTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``aspect_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAspectTypes`` requests and continue to iterate
    through the ``aspect_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListAspectTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., catalog.ListAspectTypesResponse],
        request: catalog.ListAspectTypesRequest,
        response: catalog.ListAspectTypesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListAspectTypesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListAspectTypesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.ListAspectTypesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[catalog.ListAspectTypesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[catalog.AspectType]:
        for page in self.pages:
            yield from page.aspect_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAspectTypesAsyncPager:
    """A pager for iterating through ``list_aspect_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListAspectTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``aspect_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAspectTypes`` requests and continue to iterate
    through the ``aspect_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListAspectTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[catalog.ListAspectTypesResponse]],
        request: catalog.ListAspectTypesRequest,
        response: catalog.ListAspectTypesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListAspectTypesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListAspectTypesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.ListAspectTypesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[catalog.ListAspectTypesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[catalog.AspectType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.aspect_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEntryGroupsPager:
    """A pager for iterating through ``list_entry_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListEntryGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entry_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEntryGroups`` requests and continue to iterate
    through the ``entry_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListEntryGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., catalog.ListEntryGroupsResponse],
        request: catalog.ListEntryGroupsRequest,
        response: catalog.ListEntryGroupsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListEntryGroupsRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListEntryGroupsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.ListEntryGroupsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[catalog.ListEntryGroupsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[catalog.EntryGroup]:
        for page in self.pages:
            yield from page.entry_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEntryGroupsAsyncPager:
    """A pager for iterating through ``list_entry_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListEntryGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entry_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEntryGroups`` requests and continue to iterate
    through the ``entry_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListEntryGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[catalog.ListEntryGroupsResponse]],
        request: catalog.ListEntryGroupsRequest,
        response: catalog.ListEntryGroupsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListEntryGroupsRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListEntryGroupsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.ListEntryGroupsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[catalog.ListEntryGroupsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[catalog.EntryGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entry_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEntriesPager:
    """A pager for iterating through ``list_entries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListEntriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEntries`` requests and continue to iterate
    through the ``entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListEntriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., catalog.ListEntriesResponse],
        request: catalog.ListEntriesRequest,
        response: catalog.ListEntriesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListEntriesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListEntriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.ListEntriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[catalog.ListEntriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[catalog.Entry]:
        for page in self.pages:
            yield from page.entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEntriesAsyncPager:
    """A pager for iterating through ``list_entries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListEntriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEntries`` requests and continue to iterate
    through the ``entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListEntriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[catalog.ListEntriesResponse]],
        request: catalog.ListEntriesRequest,
        response: catalog.ListEntriesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListEntriesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListEntriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.ListEntriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[catalog.ListEntriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[catalog.Entry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchEntriesPager:
    """A pager for iterating through ``search_entries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.SearchEntriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchEntries`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.SearchEntriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., catalog.SearchEntriesResponse],
        request: catalog.SearchEntriesRequest,
        response: catalog.SearchEntriesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.SearchEntriesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.SearchEntriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.SearchEntriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[catalog.SearchEntriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[catalog.SearchEntriesResult]:
        for page in self.pages:
            yield from page.results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchEntriesAsyncPager:
    """A pager for iterating through ``search_entries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.SearchEntriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchEntries`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.SearchEntriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[catalog.SearchEntriesResponse]],
        request: catalog.SearchEntriesRequest,
        response: catalog.SearchEntriesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.SearchEntriesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.SearchEntriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = catalog.SearchEntriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[catalog.SearchEntriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[catalog.SearchEntriesResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
