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
from google.cloud.speech_v2 import gapic_version as package_version

__version__ = package_version.__version__


from .services.speech import SpeechAsyncClient, SpeechClient
from .types.cloud_speech import (
    AutoDetectDecodingConfig,
    BatchRecognizeFileMetadata,
    BatchRecognizeFileResult,
    BatchRecognizeMetadata,
    BatchRecognizeRequest,
    BatchRecognizeResponse,
    BatchRecognizeResults,
    BatchRecognizeTranscriptionMetadata,
    CloudStorageResult,
    Config,
    CreateCustomClassRequest,
    CreatePhraseSetRequest,
    CreateRecognizerRequest,
    CustomClass,
    DeleteCustomClassRequest,
    DeletePhraseSetRequest,
    DeleteRecognizerRequest,
    ExplicitDecodingConfig,
    GcsOutputConfig,
    GetConfigRequest,
    GetCustomClassRequest,
    GetPhraseSetRequest,
    GetRecognizerRequest,
    InlineOutputConfig,
    InlineResult,
    ListCustomClassesRequest,
    ListCustomClassesResponse,
    ListPhraseSetsRequest,
    ListPhraseSetsResponse,
    ListRecognizersRequest,
    ListRecognizersResponse,
    NativeOutputFileFormatConfig,
    OperationMetadata,
    OutputFormatConfig,
    PhraseSet,
    RecognitionConfig,
    RecognitionFeatures,
    RecognitionOutputConfig,
    RecognitionResponseMetadata,
    Recognizer,
    RecognizeRequest,
    RecognizeResponse,
    SpeakerDiarizationConfig,
    SpeechAdaptation,
    SpeechRecognitionAlternative,
    SpeechRecognitionResult,
    SrtOutputFileFormatConfig,
    StreamingRecognitionConfig,
    StreamingRecognitionFeatures,
    StreamingRecognitionResult,
    StreamingRecognizeRequest,
    StreamingRecognizeResponse,
    TranscriptNormalization,
    UndeleteCustomClassRequest,
    UndeletePhraseSetRequest,
    UndeleteRecognizerRequest,
    UpdateConfigRequest,
    UpdateCustomClassRequest,
    UpdatePhraseSetRequest,
    UpdateRecognizerRequest,
    VttOutputFileFormatConfig,
    WordInfo,
)

__all__ = (
    "SpeechAsyncClient",
    "AutoDetectDecodingConfig",
    "BatchRecognizeFileMetadata",
    "BatchRecognizeFileResult",
    "BatchRecognizeMetadata",
    "BatchRecognizeRequest",
    "BatchRecognizeResponse",
    "BatchRecognizeResults",
    "BatchRecognizeTranscriptionMetadata",
    "CloudStorageResult",
    "Config",
    "CreateCustomClassRequest",
    "CreatePhraseSetRequest",
    "CreateRecognizerRequest",
    "CustomClass",
    "DeleteCustomClassRequest",
    "DeletePhraseSetRequest",
    "DeleteRecognizerRequest",
    "ExplicitDecodingConfig",
    "GcsOutputConfig",
    "GetConfigRequest",
    "GetCustomClassRequest",
    "GetPhraseSetRequest",
    "GetRecognizerRequest",
    "InlineOutputConfig",
    "InlineResult",
    "ListCustomClassesRequest",
    "ListCustomClassesResponse",
    "ListPhraseSetsRequest",
    "ListPhraseSetsResponse",
    "ListRecognizersRequest",
    "ListRecognizersResponse",
    "NativeOutputFileFormatConfig",
    "OperationMetadata",
    "OutputFormatConfig",
    "PhraseSet",
    "RecognitionConfig",
    "RecognitionFeatures",
    "RecognitionOutputConfig",
    "RecognitionResponseMetadata",
    "RecognizeRequest",
    "RecognizeResponse",
    "Recognizer",
    "SpeakerDiarizationConfig",
    "SpeechAdaptation",
    "SpeechClient",
    "SpeechRecognitionAlternative",
    "SpeechRecognitionResult",
    "SrtOutputFileFormatConfig",
    "StreamingRecognitionConfig",
    "StreamingRecognitionFeatures",
    "StreamingRecognitionResult",
    "StreamingRecognizeRequest",
    "StreamingRecognizeResponse",
    "TranscriptNormalization",
    "UndeleteCustomClassRequest",
    "UndeletePhraseSetRequest",
    "UndeleteRecognizerRequest",
    "UpdateConfigRequest",
    "UpdateCustomClassRequest",
    "UpdatePhraseSetRequest",
    "UpdateRecognizerRequest",
    "VttOutputFileFormatConfig",
    "WordInfo",
)
