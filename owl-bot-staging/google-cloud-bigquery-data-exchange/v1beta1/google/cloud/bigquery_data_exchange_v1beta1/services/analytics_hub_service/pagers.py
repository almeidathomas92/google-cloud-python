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
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.bigquery_data_exchange_v1beta1.types import dataexchange


class ListDataExchangesPager:
    """A pager for iterating through ``list_data_exchanges`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_exchanges`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataExchanges`` requests and continue to iterate
    through the ``data_exchanges`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., dataexchange.ListDataExchangesResponse],
            request: dataexchange.ListDataExchangesRequest,
            response: dataexchange.ListDataExchangesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesRequest):
                The initial request object.
            response (google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = dataexchange.ListDataExchangesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataexchange.ListDataExchangesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[dataexchange.DataExchange]:
        for page in self.pages:
            yield from page.data_exchanges

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListDataExchangesAsyncPager:
    """A pager for iterating through ``list_data_exchanges`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_exchanges`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataExchanges`` requests and continue to iterate
    through the ``data_exchanges`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[dataexchange.ListDataExchangesResponse]],
            request: dataexchange.ListDataExchangesRequest,
            response: dataexchange.ListDataExchangesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesRequest):
                The initial request object.
            response (google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = dataexchange.ListDataExchangesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataexchange.ListDataExchangesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[dataexchange.DataExchange]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_exchanges:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListOrgDataExchangesPager:
    """A pager for iterating through ``list_org_data_exchanges`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_exchanges`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOrgDataExchanges`` requests and continue to iterate
    through the ``data_exchanges`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., dataexchange.ListOrgDataExchangesResponse],
            request: dataexchange.ListOrgDataExchangesRequest,
            response: dataexchange.ListOrgDataExchangesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesRequest):
                The initial request object.
            response (google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = dataexchange.ListOrgDataExchangesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataexchange.ListOrgDataExchangesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[dataexchange.DataExchange]:
        for page in self.pages:
            yield from page.data_exchanges

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListOrgDataExchangesAsyncPager:
    """A pager for iterating through ``list_org_data_exchanges`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_exchanges`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOrgDataExchanges`` requests and continue to iterate
    through the ``data_exchanges`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[dataexchange.ListOrgDataExchangesResponse]],
            request: dataexchange.ListOrgDataExchangesRequest,
            response: dataexchange.ListOrgDataExchangesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesRequest):
                The initial request object.
            response (google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = dataexchange.ListOrgDataExchangesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataexchange.ListOrgDataExchangesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[dataexchange.DataExchange]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_exchanges:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListListingsPager:
    """A pager for iterating through ``list_listings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``listings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListListings`` requests and continue to iterate
    through the ``listings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., dataexchange.ListListingsResponse],
            request: dataexchange.ListListingsRequest,
            response: dataexchange.ListListingsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsRequest):
                The initial request object.
            response (google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = dataexchange.ListListingsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataexchange.ListListingsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[dataexchange.Listing]:
        for page in self.pages:
            yield from page.listings

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListListingsAsyncPager:
    """A pager for iterating through ``list_listings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``listings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListListings`` requests and continue to iterate
    through the ``listings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[dataexchange.ListListingsResponse]],
            request: dataexchange.ListListingsRequest,
            response: dataexchange.ListListingsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsRequest):
                The initial request object.
            response (google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = dataexchange.ListListingsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataexchange.ListListingsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[dataexchange.Listing]:
        async def async_generator():
            async for page in self.pages:
                for response in page.listings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
