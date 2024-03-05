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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.retail_v2.types import common

__protobuf__ = proto.module(
    package="google.cloud.retail.v2",
    manifest={
        "CompleteQueryRequest",
        "CompleteQueryResponse",
    },
)


class CompleteQueryRequest(proto.Message):
    r"""Autocomplete parameters.

    Attributes:
        catalog (str):
            Required. Catalog for which the completion is performed.

            Full resource name of catalog, such as
            ``projects/*/locations/global/catalogs/default_catalog``.
        query (str):
            Required. The query used to generate
            suggestions.
            The maximum number of allowed characters is 255.
        visitor_id (str):
            Required field. A unique identifier for tracking visitors.
            For example, this could be implemented with an HTTP cookie,
            which should be able to uniquely identify a visitor on a
            single device. This unique identifier should not change if
            the visitor logs in or out of the website.

            The field must be a UTF-8 encoded string with a length limit
            of 128 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.
        language_codes (MutableSequence[str]):
            Note that this field applies for ``user-data`` dataset only.
            For requests with ``cloud-retail`` dataset, setting this
            field has no effect.

            The language filters applied to the output suggestions. If
            set, it should contain the language of the query. If not
            set, suggestions are returned without considering language
            restrictions. This is the BCP-47 language code, such as
            "en-US" or "sr-Latn". For more information, see `Tags for
            Identifying
            Languages <https://tools.ietf.org/html/bcp47>`__. The
            maximum number of language codes is 3.
        device_type (str):
            The device type context for completion suggestions. We
            recommend that you leave this field empty.

            It can apply different suggestions on different device
            types, e.g. ``DESKTOP``, ``MOBILE``. If it is empty, the
            suggestions are across all device types.

            Supported formats:

            -  ``UNKNOWN_DEVICE_TYPE``

            -  ``DESKTOP``

            -  ``MOBILE``

            -  A customized string starts with ``OTHER_``, e.g.
               ``OTHER_IPHONE``.
        dataset (str):
            Determines which dataset to use for fetching completion.
            "user-data" will use the imported dataset through
            [CompletionService.ImportCompletionData][google.cloud.retail.v2.CompletionService.ImportCompletionData].
            "cloud-retail" will use the dataset generated by cloud
            retail based on user events. If leave empty, it will use the
            "user-data".

            Current supported values:

            -  user-data

            -  cloud-retail: This option requires enabling auto-learning
               function first. See
               `guidelines <https://cloud.google.com/retail/docs/completion-overview#generated-completion-dataset>`__.
        max_suggestions (int):
            Completion max suggestions. If left unset or set to 0, then
            will fallback to the configured value
            [CompletionConfig.max_suggestions][google.cloud.retail.v2.CompletionConfig.max_suggestions].

            The maximum allowed max suggestions is 20. If it is set
            higher, it will be capped by 20.
        entity (str):
            The entity for customers that may run multiple different
            entities, domains, sites or regions, for example,
            ``Google US``, ``Google Ads``, ``Waymo``, ``google.com``,
            ``youtube.com``, etc. If this is set, it should be exactly
            matched with
            [UserEvent.entity][google.cloud.retail.v2.UserEvent.entity]
            to get per-entity autocomplete results.
    """

    catalog: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    visitor_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    language_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    device_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    dataset: str = proto.Field(
        proto.STRING,
        number=6,
    )
    max_suggestions: int = proto.Field(
        proto.INT32,
        number=5,
    )
    entity: str = proto.Field(
        proto.STRING,
        number=10,
    )


class CompleteQueryResponse(proto.Message):
    r"""Response of the autocomplete query.

    Attributes:
        completion_results (MutableSequence[google.cloud.retail_v2.types.CompleteQueryResponse.CompletionResult]):
            Results of the matching suggestions. The
            result list is ordered and the first result is
            top suggestion.
        attribution_token (str):
            A unique complete token. This should be included in the
            [UserEvent.completion_detail][google.cloud.retail.v2.UserEvent.completion_detail]
            for search events resulting from this completion, which
            enables accurate attribution of complete model performance.
        recent_search_results (MutableSequence[google.cloud.retail_v2.types.CompleteQueryResponse.RecentSearchResult]):
            Matched recent searches of this user. The maximum number of
            recent searches is 10. This field is a restricted feature.
            Contact Retail Search support team if you are interested in
            enabling it.

            This feature is only available when
            [CompleteQueryRequest.visitor_id][google.cloud.retail.v2.CompleteQueryRequest.visitor_id]
            field is set and
            [UserEvent][google.cloud.retail.v2.UserEvent] is imported.
            The recent searches satisfy the follow rules:

            -  They are ordered from latest to oldest.

            -  They are matched with
               [CompleteQueryRequest.query][google.cloud.retail.v2.CompleteQueryRequest.query]
               case insensitively.

            -  They are transformed to lower case.

            -  They are UTF-8 safe.

            Recent searches are deduplicated. More recent searches will
            be reserved when duplication happens.
    """

    class CompletionResult(proto.Message):
        r"""Resource that represents completion results.

        Attributes:
            suggestion (str):
                The suggestion for the query.
            attributes (MutableMapping[str, google.cloud.retail_v2.types.CustomAttribute]):
                Custom attributes for the suggestion term.

                -  For "user-data", the attributes are additional custom
                   attributes ingested through BigQuery.

                -  For "cloud-retail", the attributes are product attributes
                   generated by Cloud Retail. It requires
                   [UserEvent.product_details][google.cloud.retail.v2.UserEvent.product_details]
                   is imported properly.
        """

        suggestion: str = proto.Field(
            proto.STRING,
            number=1,
        )
        attributes: MutableMapping[str, common.CustomAttribute] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=2,
            message=common.CustomAttribute,
        )

    class RecentSearchResult(proto.Message):
        r"""Recent search of this user.

        Attributes:
            recent_search (str):
                The recent search query.
        """

        recent_search: str = proto.Field(
            proto.STRING,
            number=1,
        )

    completion_results: MutableSequence[CompletionResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CompletionResult,
    )
    attribution_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    recent_search_results: MutableSequence[RecentSearchResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=RecentSearchResult,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
