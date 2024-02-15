# Changelog

## [0.3.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.3.4...google-cloud-datacatalog-lineage-v0.3.5) (2024-02-15)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12282](https://github.com/googleapis/google-cloud-python/issues/12282)) ([b985096](https://github.com/googleapis/google-cloud-python/commit/b985096d43add8214172ff993e00293e6c8757cb))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12305](https://github.com/googleapis/google-cloud-python/issues/12305)) ([2aa7f17](https://github.com/googleapis/google-cloud-python/commit/2aa7f17a5fd4f2249260225db91fb0414d06eaa7))

## [0.3.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.3.3...google-cloud-datacatalog-lineage-v0.3.4) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))

## [0.3.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.3.2...google-cloud-datacatalog-lineage-v0.3.3) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12239](https://github.com/googleapis/google-cloud-python/issues/12239)) ([8004d15](https://github.com/googleapis/google-cloud-python/commit/8004d15d9e6baa4dc5bc3f09d528e176d54d9ec5))

## [0.3.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.3.1...google-cloud-datacatalog-lineage-v0.3.2) (2023-12-07)


### Features

* Add support for python 3.12 ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))
* Introduce compatibility with native namespace packages ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))
* Use `retry_async` instead of `retry` in async client ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))

## [0.3.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.3.0...google-cloud-datacatalog-lineage-v0.3.1) (2023-11-07)


### Features

* add open lineage support ([079b58a](https://github.com/googleapis/google-cloud-python/commit/079b58af418cfcc036885280595efad0b7bb164f))


### Bug Fixes

* change `start_time` in message `.google.cloud.datacatalog.lineage.v1.LineageEvent` to `required` as intended by api ([079b58a](https://github.com/googleapis/google-cloud-python/commit/079b58af418cfcc036885280595efad0b7bb164f))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.2.4...google-cloud-datacatalog-lineage-v0.3.0) (2023-11-02)


### ⚠ BREAKING CHANGES

* Use `google.cloud.datacatalog_lineage` to avoid conflict with `google.cloud.datacatalog` ([#11944](https://github.com/googleapis/google-cloud-python/issues/11944))

### Bug Fixes

* Use `google.cloud.datacatalog_lineage` to avoid conflict with `google.cloud.datacatalog` ([#11944](https://github.com/googleapis/google-cloud-python/issues/11944)) ([3059986](https://github.com/googleapis/google-cloud-python/commit/3059986d22adb354a303f67bb254ef8343ed7453))

## [0.2.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.2.3...google-cloud-datacatalog-lineage-v0.2.4) (2023-09-19)


### Documentation

* Minor formatting ([9487380](https://github.com/googleapis/google-cloud-python/commit/94873808ece8059b07644a0a49dedf8e2906900a))

## [0.2.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.2.2...google-cloud-datacatalog-lineage-v0.2.3) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11445](https://github.com/googleapis/google-cloud-python/issues/11445)) ([98bddda](https://github.com/googleapis/google-cloud-python/commit/98bdddafc821e2fc6e86a31965da0c46899aa229))

## [0.2.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.2.1...google-cloud-datacatalog-lineage-v0.2.2) (2023-03-25)


### Documentation

* Fix formatting of request arg in docstring ([#10867](https://github.com/googleapis/google-cloud-python/issues/10867)) ([d34a425](https://github.com/googleapis/google-cloud-python/commit/d34a425f7d0f02bebaf20d24b725b8c25c699697))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-datacatalog-lineage-v0.2.0...google-cloud-datacatalog-lineage-v0.2.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([900a608](https://github.com/googleapis/google-cloud-python/commit/900a6083e59bfebf215e4e469bc842d8788bba18))


### Documentation

* Add documentation for enums ([900a608](https://github.com/googleapis/google-cloud-python/commit/900a6083e59bfebf215e4e469bc842d8788bba18))

## 0.2.0 (2023-01-12)


### Features

* add initial files for google.cloud.datacatalog.lineage.v1 ([3873233](https://github.com/googleapis/google-cloud-python/commit/3873233f28ed25f99dada66dfa83edbf7043e7b5))

## Changelog
