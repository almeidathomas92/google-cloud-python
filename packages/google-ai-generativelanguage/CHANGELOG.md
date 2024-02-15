# Changelog

## [0.5.3](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.5.2...google-ai-generativelanguage-v0.5.3) (2024-02-15)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12280](https://github.com/googleapis/google-cloud-python/issues/12280)) ([2d75d0e](https://github.com/googleapis/google-cloud-python/commit/2d75d0e67ca4cccddc688bd37c14ac80564a2e65))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12303](https://github.com/googleapis/google-cloud-python/issues/12303)) ([fbb80c3](https://github.com/googleapis/google-cloud-python/commit/fbb80c32f7db91e25bd1cc30966f630728ff6d6a))

## [0.5.2](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.5.1...google-ai-generativelanguage-v0.5.2) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))

## [0.5.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.5.0...google-ai-generativelanguage-v0.5.1) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([a0392ee](https://github.com/googleapis/google-cloud-python/commit/a0392eeb59fcc6ea7c55283110b92aa24a4d40a0))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.4.1...google-ai-generativelanguage-v0.5.0) (2024-01-24)


### ⚠ BREAKING CHANGES

* Fix content.proto's Schema - `type` should be required

### Features

* Update GenAI libraries to include input_safety_feedback ([d2004d4](https://github.com/googleapis/google-cloud-python/commit/d2004d4a1c95333017b585ba905d5e0c4af45776))


### Bug Fixes

* Fix content.proto's Schema - `type` should be required ([d2004d4](https://github.com/googleapis/google-cloud-python/commit/d2004d4a1c95333017b585ba905d5e0c4af45776))


### Documentation

* Minor docs updates ([d2004d4](https://github.com/googleapis/google-cloud-python/commit/d2004d4a1c95333017b585ba905d5e0c4af45776))
* Update summary, improve description for `title` in `EmbedContentRequest` ([d2004d4](https://github.com/googleapis/google-cloud-python/commit/d2004d4a1c95333017b585ba905d5e0c4af45776))

## [0.4.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.4.0...google-ai-generativelanguage-v0.4.1) (2024-01-22)


### Documentation

* [google-ai-generativelanguage] Fixed minor documentation typos for field `function_declarations` in message `google.ai.generativelanguage.v1beta.Tool` ([#12206](https://github.com/googleapis/google-cloud-python/issues/12206)) ([52957f3](https://github.com/googleapis/google-cloud-python/commit/52957f38e2d5dca5e873cfc7239a6ce469ed541f))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.5...google-ai-generativelanguage-v0.4.0) (2023-12-09)


### Features

* Add v1, contains only GenerativeService, nothing else ([23d8814](https://github.com/googleapis/google-cloud-python/commit/23d8814baa6288d94484d52a98714fd32755ada3))
* Add v1beta, adds GenerativeService and RetrievalService ([23d8814](https://github.com/googleapis/google-cloud-python/commit/23d8814baa6288d94484d52a98714fd32755ada3))
* Set `google.ai.generativelanguage_v1beta` as the default import ([23d8814](https://github.com/googleapis/google-cloud-python/commit/23d8814baa6288d94484d52a98714fd32755ada3))

## [0.3.5](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.4...google-ai-generativelanguage-v0.3.5) (2023-12-07)


### Features

* Add support for python 3.12 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Introduce compatibility with native namespace packages ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Use `retry_async` instead of `retry` in async client ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))

## [0.3.4](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.3...google-ai-generativelanguage-v0.3.4) (2023-09-30)


### Documentation

* Minor formatting ([#11630](https://github.com/googleapis/google-cloud-python/issues/11630)) ([b176996](https://github.com/googleapis/google-cloud-python/commit/b176996309cb5b3e9c257caaebde8884bd556824))

## [0.3.3](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.2...google-ai-generativelanguage-v0.3.3) (2023-09-21)


### Bug Fixes

* set google.ai.generativelanguage_v1beta3 as the default import ([#11677](https://github.com/googleapis/google-cloud-python/issues/11677)) ([39ea699](https://github.com/googleapis/google-cloud-python/commit/39ea699f6c3957f2ae20990555b9f47c1b285f31))

## [0.3.2](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.1...google-ai-generativelanguage-v0.3.2) (2023-09-20)


### Features

* Add BatchEmbedText and CountTextTokens to the text service ([38f2ca3](https://github.com/googleapis/google-cloud-python/commit/38f2ca3b3356c0fb42ebdf341dd548836c0896f3))
* Add google/ai/generativelanguage_v1beta3  ([38f2ca3](https://github.com/googleapis/google-cloud-python/commit/38f2ca3b3356c0fb42ebdf341dd548836c0896f3))
* Add model tuning ([38f2ca3](https://github.com/googleapis/google-cloud-python/commit/38f2ca3b3356c0fb42ebdf341dd548836c0896f3))
* Add permissions service ([38f2ca3](https://github.com/googleapis/google-cloud-python/commit/38f2ca3b3356c0fb42ebdf341dd548836c0896f3))

## [0.3.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.0...google-ai-generativelanguage-v0.3.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11444](https://github.com/googleapis/google-cloud-python/issues/11444)) ([9aa301a](https://github.com/googleapis/google-cloud-python/commit/9aa301ae6ca3080cae286a19de9cdc1b796ab37d))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.2.1...google-ai-generativelanguage-v0.3.0) (2023-06-29)


### Bug Fixes

* remove `BLOCK_NONE` from `HarmBlockThreshold` ([9d46f7f](https://github.com/googleapis/google-cloud-python/commit/9d46f7f5c6d2f84b8e351969d4ab17b4195b941b))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.2.0...google-ai-generativelanguage-v0.2.1) (2023-06-03)


### Documentation

* fix broken client library documentation links ([#11192](https://github.com/googleapis/google-cloud-python/issues/11192)) ([5e17f7a](https://github.com/googleapis/google-cloud-python/commit/5e17f7a901bbbae8ff9a44ed62f1abd2386da2c8))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.1.0...google-ai-generativelanguage-v0.2.0) (2023-05-05)


### Features

* Add safety settings ([#11148](https://github.com/googleapis/google-cloud-python/issues/11148)) ([f9544c9](https://github.com/googleapis/google-cloud-python/commit/f9544c9897dd4d010c5b8703c744d8f28ae3b070))

## 0.1.0 (2023-05-02)


### Features

* add initial files for google.ai.generativelanguage.v1beta2 ([#11142](https://github.com/googleapis/google-cloud-python/issues/11142)) ([54363fd](https://github.com/googleapis/google-cloud-python/commit/54363fd60decdecb05302fc9bce8e278eb39951e))

## Changelog
