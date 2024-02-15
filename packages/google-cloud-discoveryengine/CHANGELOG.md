# Changelog

## [0.11.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.11.7...google-cloud-discoveryengine-v0.11.8) (2024-02-15)


### Features

* Add data store, engine, serving config and site search engine services  ([00cf69e](https://github.com/googleapis/google-cloud-python/commit/00cf69ee2536bda6a2ccc086343d4be2744e7303))
* Add engine support for multi-turn search and search APIs ([00cf69e](https://github.com/googleapis/google-cloud-python/commit/00cf69ee2536bda6a2ccc086343d4be2744e7303))
* Add suggestion deny list import/purge APIs ([00cf69e](https://github.com/googleapis/google-cloud-python/commit/00cf69ee2536bda6a2ccc086343d4be2744e7303))
* Support search summarization with citations and references ([00cf69e](https://github.com/googleapis/google-cloud-python/commit/00cf69ee2536bda6a2ccc086343d4be2744e7303))


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12282](https://github.com/googleapis/google-cloud-python/issues/12282)) ([b985096](https://github.com/googleapis/google-cloud-python/commit/b985096d43add8214172ff993e00293e6c8757cb))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12306](https://github.com/googleapis/google-cloud-python/issues/12306)) ([1e787f2](https://github.com/googleapis/google-cloud-python/commit/1e787f2079ac41ce634c7b90f02a6597cecb64be))


### Documentation

* Keep the API doc up-to-date with recent changes ([00cf69e](https://github.com/googleapis/google-cloud-python/commit/00cf69ee2536bda6a2ccc086343d4be2744e7303))

## [0.11.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.11.6...google-cloud-discoveryengine-v0.11.7) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))

## [0.11.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.11.5...google-cloud-discoveryengine-v0.11.6) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12240](https://github.com/googleapis/google-cloud-python/issues/12240)) ([d51f832](https://github.com/googleapis/google-cloud-python/commit/d51f83298f89dbae23af1a146411b296eba6bba2))

## [0.11.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.11.4...google-cloud-discoveryengine-v0.11.5) (2023-12-13)


### Features

* **v1alpha:** add engine support for conversational engine service ([9b171b1](https://github.com/googleapis/google-cloud-python/commit/9b171b158ebdb4d10feb4c0faed6407a9023c3a8))
* **v1alpha:** add search tuning service ([9b171b1](https://github.com/googleapis/google-cloud-python/commit/9b171b158ebdb4d10feb4c0faed6407a9023c3a8))
* **v1alpha:** add site search engine service ([9b171b1](https://github.com/googleapis/google-cloud-python/commit/9b171b158ebdb4d10feb4c0faed6407a9023c3a8))
* **v1alpha:** support search summarization with citations and references ([9b171b1](https://github.com/googleapis/google-cloud-python/commit/9b171b158ebdb4d10feb4c0faed6407a9023c3a8))


### Documentation

* **v1alpha:** keep the API doc up-to-date with recent changes ([9b171b1](https://github.com/googleapis/google-cloud-python/commit/9b171b158ebdb4d10feb4c0faed6407a9023c3a8))

## [0.11.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.11.3...google-cloud-discoveryengine-v0.11.4) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [0.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.11.2...google-cloud-discoveryengine-v0.11.3) (2023-11-13)


### Features

* [google-cloud-discoveryengine] add data store and engine services ([#12017](https://github.com/googleapis/google-cloud-python/issues/12017)) ([ac7c891](https://github.com/googleapis/google-cloud-python/commit/ac7c891c50de4f95f0253c6716482bbb78696793))

## [0.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.11.1...google-cloud-discoveryengine-v0.11.2) (2023-10-10)


### Features

* add v1alpha public library for discoveryengine ([#11796](https://github.com/googleapis/google-cloud-python/issues/11796)) ([e9ccb06](https://github.com/googleapis/google-cloud-python/commit/e9ccb06149480b1e21523e666e4bcb7f2cc2c5ed))

## [0.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.11.0...google-cloud-discoveryengine-v0.11.1) (2023-09-19)


### Documentation

* Minor formatting ([#11632](https://github.com/googleapis/google-cloud-python/issues/11632)) ([dbee08f](https://github.com/googleapis/google-cloud-python/commit/dbee08f2df63e1906ba13b0d3060eec5a80c79e2))

## [0.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.10.0...google-cloud-discoveryengine-v0.11.0) (2023-08-31)


### Features

* added more options for search extractive content support ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* added more skip reasons and details for search summarization ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* added query expansion details in search response ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* allow uri in user events ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* support bring your own embedding feature ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* support conversational / multi-turn search ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* support image search ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* support search summarization ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* support structural search features ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* support tail suggestions in completion API ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))
* updated summarization interface for multi-turn search ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))


### Documentation

* keep the API doc up-to-date with recent changes ([1b1f1b3](https://github.com/googleapis/google-cloud-python/commit/1b1f1b3a0f6775443658bcf129e396a68dbde097))

## [0.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.9.1...google-cloud-discoveryengine-v0.10.0) (2023-08-03)


### Features

* add skip reason for search summarization ([2058c1f](https://github.com/googleapis/google-cloud-python/commit/2058c1f5ea631c943df19243472eb9a26c08dede))
* support conversational / multi-turn search ([2058c1f](https://github.com/googleapis/google-cloud-python/commit/2058c1f5ea631c943df19243472eb9a26c08dede))
* support image search ([2058c1f](https://github.com/googleapis/google-cloud-python/commit/2058c1f5ea631c943df19243472eb9a26c08dede))
* support tail suggestions in completion API ([2058c1f](https://github.com/googleapis/google-cloud-python/commit/2058c1f5ea631c943df19243472eb9a26c08dede))


### Documentation

* keep the API doc up-to-date with recent changes ([2058c1f](https://github.com/googleapis/google-cloud-python/commit/2058c1f5ea631c943df19243472eb9a26c08dede))

## [0.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.9.0...google-cloud-discoveryengine-v0.9.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11446](https://github.com/googleapis/google-cloud-python/issues/11446)) ([37682b7](https://github.com/googleapis/google-cloud-python/commit/37682b7793cfe0dcb27963fea7e474b3b85571c9))

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.8.1...google-cloud-discoveryengine-v0.9.0) (2023-06-19)


### Features

* add `redirect_uri` in search response ([7c48e6a](https://github.com/googleapis/google-cloud-python/commit/7c48e6aabe63630b3bc23e5168a99df7757bd2a5))
* support docx/pptx/txt/csv in allowed data format ([7c48e6a](https://github.com/googleapis/google-cloud-python/commit/7c48e6aabe63630b3bc23e5168a99df7757bd2a5))
* support extractive content in search ([7c48e6a](https://github.com/googleapis/google-cloud-python/commit/7c48e6aabe63630b3bc23e5168a99df7757bd2a5))


### Documentation

* keep the API doc up-to-date with recent changes ([7c48e6a](https://github.com/googleapis/google-cloud-python/commit/7c48e6aabe63630b3bc23e5168a99df7757bd2a5))

## [0.8.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.8.0...google-cloud-discoveryengine-v0.8.1) (2023-06-07)


### Bug Fixes

* remove the summarization feature from v1 version ([#11375](https://github.com/googleapis/google-cloud-python/issues/11375)) ([9336efb](https://github.com/googleapis/google-cloud-python/commit/9336efb52d32d1e29a0a71c81c80fb64e448cac1))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.7.0...google-cloud-discoveryengine-v0.8.0) (2023-05-25)


### Features

* **v1:** add discovery engine v1 client library ([10671ec](https://github.com/googleapis/google-cloud-python/commit/10671ec9c0b16892100f2c91a6138571fabcbeb2))
* **v1beta:** add LRO API for schema service ([10671ec](https://github.com/googleapis/google-cloud-python/commit/10671ec9c0b16892100f2c91a6138571fabcbeb2))
* **v1beta:** allow users to specify id field in documents gcs import ([10671ec](https://github.com/googleapis/google-cloud-python/commit/10671ec9c0b16892100f2c91a6138571fabcbeb2))


### Documentation

* **v1beta:** keep the API doc up-to-date with recent changes ([10671ec](https://github.com/googleapis/google-cloud-python/commit/10671ec9c0b16892100f2c91a6138571fabcbeb2))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.6.0...google-cloud-discoveryengine-v0.7.0) (2023-05-17)


### Features

* allow users to provide additional labels in search ([c6addce](https://github.com/googleapis/google-cloud-python/commit/c6addce5b9281c75db2c7e96d7a57cb202d48006))
* allow users to provide user info in search ([c6addce](https://github.com/googleapis/google-cloud-python/commit/c6addce5b9281c75db2c7e96d7a57cb202d48006))
* enable safe search feature for site search ([c6addce](https://github.com/googleapis/google-cloud-python/commit/c6addce5b9281c75db2c7e96d7a57cb202d48006))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.5.0...google-cloud-discoveryengine-v0.6.0) (2023-05-04)


### Features

* add document purge API ([#11140](https://github.com/googleapis/google-cloud-python/issues/11140)) ([1115310](https://github.com/googleapis/google-cloud-python/commit/1115310f07f767a5c6fac5831e046aa9e879f0ea))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.4.1...google-cloud-discoveryengine-v0.5.0) (2023-04-21)


### Features

* add search, autocomplete and schema services ([5e1e0af](https://github.com/googleapis/google-cloud-python/commit/5e1e0af0dadd3bd801664c7d315b743a4dbf7b0b))
* add unstructured document support (PDF/HTML) ([5e1e0af](https://github.com/googleapis/google-cloud-python/commit/5e1e0af0dadd3bd801664c7d315b743a4dbf7b0b))


### Documentation

* keep the API doc up-to-date with recent changes ([5e1e0af](https://github.com/googleapis/google-cloud-python/commit/5e1e0af0dadd3bd801664c7d315b743a4dbf7b0b))

## [0.4.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.4.0...google-cloud-discoveryengine-v0.4.1) (2023-03-25)


### Documentation

* Fix formatting of request arg in docstring ([#10867](https://github.com/googleapis/google-cloud-python/issues/10867)) ([d34a425](https://github.com/googleapis/google-cloud-python/commit/d34a425f7d0f02bebaf20d24b725b8c25c699697))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.3.1...google-cloud-discoveryengine-v0.4.0) (2023-03-22)


### Features

* add additional resource path with collections ([68d329e](https://github.com/googleapis/google-cloud-python/commit/68d329e886be89629c1961ee87e0b1123f3feda4))
* document schema id is no longer required ([68d329e](https://github.com/googleapis/google-cloud-python/commit/68d329e886be89629c1961ee87e0b1123f3feda4))


### Documentation

* keep the API doc up-to-date with recent changes ([68d329e](https://github.com/googleapis/google-cloud-python/commit/68d329e886be89629c1961ee87e0b1123f3feda4))

## [0.3.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.3.0...google-cloud-discoveryengine-v0.3.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([900a608](https://github.com/googleapis/google-cloud-python/commit/900a6083e59bfebf215e4e469bc842d8788bba18))


### Documentation

* Add documentation for enums ([900a608](https://github.com/googleapis/google-cloud-python/commit/900a6083e59bfebf215e4e469bc842d8788bba18))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.2.1...google-cloud-discoveryengine-v0.3.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#10812](https://github.com/googleapis/google-cloud-python/issues/10812)) ([e5f88ee](https://github.com/googleapis/google-cloud-python/commit/e5f88eebd47c677850d61ddc3774532723f5505e))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.2.0...google-cloud-discoveryengine-v0.2.1) (2022-12-06)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))
* Drop usage of pkg_resources ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))
* Fix timeout default values ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.1.1...google-cloud-discoveryengine-v0.2.0) (2022-11-10)


### Features

* Add typing to proto.Message based class attributes ([a6cbc16](https://github.com/googleapis/google-cloud-python/commit/a6cbc167835880f9fe31b4030ec5fba69e35b383))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([a6cbc16](https://github.com/googleapis/google-cloud-python/commit/a6cbc167835880f9fe31b4030ec5fba69e35b383))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-discoveryengine-v0.1.0...google-cloud-discoveryengine-v0.1.1) (2022-11-02)


### Features

* add initial files for google.cloud.discoveryengine.v1beta ([84b3b3b](https://github.com/googleapis/google-cloud-python/commit/84b3b3b126dab3e5cbab316350ccc1ca457e8742))

## Changelog
