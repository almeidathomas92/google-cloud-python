# Changelog

## [0.17.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.11...google-cloud-batch-v0.17.12) (2024-02-15)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12280](https://github.com/googleapis/google-cloud-python/issues/12280)) ([2d75d0e](https://github.com/googleapis/google-cloud-python/commit/2d75d0e67ca4cccddc688bd37c14ac80564a2e65))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12304](https://github.com/googleapis/google-cloud-python/issues/12304)) ([c52e0cd](https://github.com/googleapis/google-cloud-python/commit/c52e0cdbddf44c96f642d8d596c5413c4006ba82))

## [0.17.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.10...google-cloud-batch-v0.17.11) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))

## [0.17.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.9...google-cloud-batch-v0.17.10) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([a0392ee](https://github.com/googleapis/google-cloud-python/commit/a0392eeb59fcc6ea7c55283110b92aa24a4d40a0))

## [0.17.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.8...google-cloud-batch-v0.17.9) (2024-01-24)


### Features

* Add `run_as_non_root` field to allow user's runnable be executed as non root ([7d78274](https://github.com/googleapis/google-cloud-python/commit/7d78274ac9fb2f535e222c538d7908d8705a3314))
* Add `tags` field in Job's AllocationPolicy field in v1 ([7d78274](https://github.com/googleapis/google-cloud-python/commit/7d78274ac9fb2f535e222c538d7908d8705a3314))
* Add Batch Image Streaming support for v1 ([7d78274](https://github.com/googleapis/google-cloud-python/commit/7d78274ac9fb2f535e222c538d7908d8705a3314))


### Documentation

* [google-cloud-batch] Polish the field descriptions for enableImageStreaming and CloudLoggingOptions ([#12216](https://github.com/googleapis/google-cloud-python/issues/12216)) ([d23ec54](https://github.com/googleapis/google-cloud-python/commit/d23ec544504af029ac9530cc5cb435eb0f02e384))

## [0.17.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.7...google-cloud-batch-v0.17.8) (2024-01-22)


### Bug Fixes

* **v1alpha:** [google-cloud-batch] remove deprecated field enableOslogin ([#12210](https://github.com/googleapis/google-cloud-python/issues/12210)) ([527862b](https://github.com/googleapis/google-cloud-python/commit/527862b9f38f9ef47b33584912d18aed191aaa6a))

## [0.17.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.6...google-cloud-batch-v0.17.7) (2024-01-12)


### Features

* Add `run_as_non_root field` and deprecate `enable_oslogin` for non-root execution ([ce7ddbf](https://github.com/googleapis/google-cloud-python/commit/ce7ddbfdb90ad6e1eb46a79ce3e12276fbfa00ba))
* Add `tags` field in Job's AllocationPolicy field in v1alpha ([ce7ddbf](https://github.com/googleapis/google-cloud-python/commit/ce7ddbfdb90ad6e1eb46a79ce3e12276fbfa00ba))


### Documentation

* updated comments ([ce7ddbf](https://github.com/googleapis/google-cloud-python/commit/ce7ddbfdb90ad6e1eb46a79ce3e12276fbfa00ba))

## [0.17.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.5...google-cloud-batch-v0.17.6) (2023-12-07)


### Features

* Add support for python 3.12 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Introduce compatibility with native namespace packages ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Use `retry_async` instead of `retry` in async client ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))

## [0.17.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.4...google-cloud-batch-v0.17.5) (2023-11-29)


### Features

* Add a CloudLoggingOption to configure additional settings for Cloud Logging ([9c53819](https://github.com/googleapis/google-cloud-python/commit/9c5381911c4eb0b0b67d116a53ed6a08e870bbe1))
* **v1alpha:** Add TaskGroup.enable_oslogin to give the Batch job submitter the ability to run runnables as non-root controlled by IAM ([5392065](https://github.com/googleapis/google-cloud-python/commit/5392065c62888a649dca0697b6e5ce3ea174ae00))


### Documentation

* Update comment for AllocationPolicy.network ([9c53819](https://github.com/googleapis/google-cloud-python/commit/9c5381911c4eb0b0b67d116a53ed6a08e870bbe1))
* **v1alpha:** Update documentation for the network field of AllocationPolicy ([5392065](https://github.com/googleapis/google-cloud-python/commit/5392065c62888a649dca0697b6e5ce3ea174ae00))

## [0.17.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.3...google-cloud-batch-v0.17.4) (2023-11-14)


### Features

* [google-cloud-batch] add a CloudLoggingOption and use_generic_task_monitored_resource fields for users to opt out new batch monitored resource in cloud logging ([#12019](https://github.com/googleapis/google-cloud-python/issues/12019)) ([13fd2e1](https://github.com/googleapis/google-cloud-python/commit/13fd2e1256668b3e5ca92bccd9029b1c41839e41))

## [0.17.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.2...google-cloud-batch-v0.17.3) (2023-11-02)


### Documentation

* Add clarification for `TaskGroup.parallelism` ([9cd9608](https://github.com/googleapis/google-cloud-python/commit/9cd960879538700dd9c843a11855c9d58bbf97f2))
* update default max parallel tasks per job ([#11940](https://github.com/googleapis/google-cloud-python/issues/11940)) ([9cd9608](https://github.com/googleapis/google-cloud-python/commit/9cd960879538700dd9c843a11855c9d58bbf97f2))

## [0.17.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.1...google-cloud-batch-v0.17.2) (2023-10-19)


### Features

* expose display_name to batch v1 API ([8235ef6](https://github.com/googleapis/google-cloud-python/commit/8235ef62943bae4bb574c4d5555ce46db231c7d2))

## [0.17.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.17.0...google-cloud-batch-v0.17.1) (2023-09-30)


### Documentation

* update batch PD interface support ([a300b07](https://github.com/googleapis/google-cloud-python/commit/a300b079de26647c09e783a9e27309290a5b4522))

## [0.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.16.0...google-cloud-batch-v0.17.0) (2023-08-31)


### Features

* add Batch Managed Container support for v1alpha ([37e457c](https://github.com/googleapis/google-cloud-python/commit/37e457c74eccc838771cba93d216afc4be97030f))
* Add more compute resource API descriptions to match with VM's machine type field ([37e457c](https://github.com/googleapis/google-cloud-python/commit/37e457c74eccc838771cba93d216afc4be97030f))
* add stderr_snippet to indicate the real stderr output by runnables to the execution field of status event ([1a8670d](https://github.com/googleapis/google-cloud-python/commit/1a8670df87e7a840cee211bbf17794dc0114d840))
* Clarify Batch API proto doc about pubsub notifications ([37e457c](https://github.com/googleapis/google-cloud-python/commit/37e457c74eccc838771cba93d216afc4be97030f))


### Documentation

* Clarify Batch API proto doc about pubsub notifications ([1a8670d](https://github.com/googleapis/google-cloud-python/commit/1a8670df87e7a840cee211bbf17794dc0114d840))
* Expand compute resource API docs to match with VM's machine type field ([1a8670d](https://github.com/googleapis/google-cloud-python/commit/1a8670df87e7a840cee211bbf17794dc0114d840))
* Update description on size_gb in disk field ([#11615](https://github.com/googleapis/google-cloud-python/issues/11615)) ([d46f714](https://github.com/googleapis/google-cloud-python/commit/d46f7142e4e50f4a3dedb01e9fa574ebb29ce50e))

## [0.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.15.0...google-cloud-batch-v0.16.0) (2023-08-09)


### Features

* Add Batch Managed Container support for v1alpha ([0e7f0b0](https://github.com/googleapis/google-cloud-python/commit/0e7f0b07e4b6149c8e573cab6f82667f1fe50cf6))
* Clarify Batch API proto doc about pubsub notifications ([0e7f0b0](https://github.com/googleapis/google-cloud-python/commit/0e7f0b07e4b6149c8e573cab6f82667f1fe50cf6))


### Documentation

* Clarify Batch API proto doc about pubsub notifications ([#11550](https://github.com/googleapis/google-cloud-python/issues/11550)) ([4a8107a](https://github.com/googleapis/google-cloud-python/commit/4a8107a7dd492249807702cdc406c9d9c294c663))

## [0.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.14.0...google-cloud-batch-v0.15.0) (2023-08-03)


### Features

* allow order_by for v1 ListJobs ([f5f6d35](https://github.com/googleapis/google-cloud-python/commit/f5f6d359cc90beb9752ac91203aeb92f9559b06d))
* Enable gpu driver version field on v1 ([f5f6d35](https://github.com/googleapis/google-cloud-python/commit/f5f6d359cc90beb9752ac91203aeb92f9559b06d))


### Documentation

* Add comment to the unsupported order_by field of ListTasksRequest ([f5f6d35](https://github.com/googleapis/google-cloud-python/commit/f5f6d359cc90beb9752ac91203aeb92f9559b06d))
* Improve url examples formats on Batch API comments ([f5f6d35](https://github.com/googleapis/google-cloud-python/commit/f5f6d359cc90beb9752ac91203aeb92f9559b06d))

## [0.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-batch-v0.13.0...google-cloud-batch-v0.14.0) (2023-07-25)


### Features

* **v1alpha:** Enable gpu driver version field ([2528a8e](https://github.com/googleapis/google-cloud-python/commit/2528a8eb35af8319f2b22d2aad7fea4697d75f87))


### Documentation

* **v1alpha:** Improve url examples in comments ([2528a8e](https://github.com/googleapis/google-cloud-python/commit/2528a8eb35af8319f2b22d2aad7fea4697d75f87))
* **v1alpha:** Mark `order_by` field in `ListTasksRequest` as not implemented. ([2528a8e](https://github.com/googleapis/google-cloud-python/commit/2528a8eb35af8319f2b22d2aad7fea4697d75f87))

## [0.13.0](https://github.com/googleapis/python-batch/compare/v0.12.0...v0.13.0) (2023-07-04)


### Features

* **v1alpha:** Add gpu driver version field ([fa1e00b](https://github.com/googleapis/python-batch/commit/fa1e00bedc7386ab6119ab79c11ec03607bb6da7))


### Bug Fixes

* Add async context manager return types ([#122](https://github.com/googleapis/python-batch/issues/122)) ([57f49cc](https://github.com/googleapis/python-batch/commit/57f49ccd10494f5ad26a592cd35e4f73bcdcdc8d))


### Documentation

* **v1:** Add image shortcut example for Batch HPC CentOS Image ([#119](https://github.com/googleapis/python-batch/issues/119)) ([cc9d65a](https://github.com/googleapis/python-batch/commit/cc9d65ad9329a3e8b281834fe32ea56ce28b5599))
* **v1alpha:** Add image shortcut example for Batch HPC CentOS Image ([fa1e00b](https://github.com/googleapis/python-batch/commit/fa1e00bedc7386ab6119ab79c11ec03607bb6da7))

## [0.12.0](https://github.com/googleapis/python-batch/compare/v0.11.0...v0.12.0) (2023-06-14)


### Features

* **v1:** Add support for scheduling_policy ([23d3a5e](https://github.com/googleapis/python-batch/commit/23d3a5ebe524426507283087b7f2529ad9de65dd))


### Documentation

* Minor clarifications for TaskGroup and min_cpu_platform ([23d3a5e](https://github.com/googleapis/python-batch/commit/23d3a5ebe524426507283087b7f2529ad9de65dd))

## [0.11.0](https://github.com/googleapis/python-batch/compare/v0.10.0...v0.11.0) (2023-05-25)


### Features

* **v1:** Add support for per-Runnable labels ([977ce57](https://github.com/googleapis/python-batch/commit/977ce57f89e15b46ead282df89ed371e68631ca6))
* **v1:** Add support for placement policies ([977ce57](https://github.com/googleapis/python-batch/commit/977ce57f89e15b46ead282df89ed371e68631ca6))
* **v1alpha:** Add support for placement policies ([be22675](https://github.com/googleapis/python-batch/commit/be226750e6783a5994a497106c87cc7183654549))
* **v1alpha:** Support order_by in ListJobs and ListTasks requests ([be22675](https://github.com/googleapis/python-batch/commit/be226750e6783a5994a497106c87cc7183654549))

## [0.10.0](https://github.com/googleapis/python-batch/compare/v0.9.0...v0.10.0) (2023-03-16)


### Features

* Added StatusEvent.task_state ([de68b7c](https://github.com/googleapis/python-batch/commit/de68b7c772bdd90f258139b7dc1f5268dfe5eb8e))


### Bug Fixes

* Remove IAM methods ([de68b7c](https://github.com/googleapis/python-batch/commit/de68b7c772bdd90f258139b7dc1f5268dfe5eb8e))


### Documentation

* Point to the correct documentation page ([#102](https://github.com/googleapis/python-batch/issues/102)) ([2d13090](https://github.com/googleapis/python-batch/commit/2d1309089dd0747f7bab08d743e971e429536393))
* Updated comments ([de68b7c](https://github.com/googleapis/python-batch/commit/de68b7c772bdd90f258139b7dc1f5268dfe5eb8e))

## [0.9.0](https://github.com/googleapis/python-batch/compare/v0.8.1...v0.9.0) (2023-02-04)


### Features

* Add boot disk field in InstancePolicy ([3a73b21](https://github.com/googleapis/python-batch/commit/3a73b21726e1780be3782fd3eb98eca28a0759f5))
* Add boot disk field in InstanceStatus ([3a73b21](https://github.com/googleapis/python-batch/commit/3a73b21726e1780be3782fd3eb98eca28a0759f5))
* Support custom scopes for service account ([3a73b21](https://github.com/googleapis/python-batch/commit/3a73b21726e1780be3782fd3eb98eca28a0759f5))

## [0.8.1](https://github.com/googleapis/python-batch/compare/v0.8.0...v0.8.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([695d075](https://github.com/googleapis/python-batch/commit/695d07584f895318358ff0315be8046d816fc2ef))


### Documentation

* Add documentation for enums ([695d075](https://github.com/googleapis/python-batch/commit/695d07584f895318358ff0315be8046d816fc2ef))

## [0.8.0](https://github.com/googleapis/python-batch/compare/v0.7.0...v0.8.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#86](https://github.com/googleapis/python-batch/issues/86)) ([4f0cb51](https://github.com/googleapis/python-batch/commit/4f0cb51cb5e6754c5b5b0cd02cb5b06a6c0ef79d))

## [0.7.0](https://github.com/googleapis/python-batch/compare/v0.6.0...v0.7.0) (2023-01-04)


### Features

* Support secret and encrypted environment variables in v1 ([711e132](https://github.com/googleapis/python-batch/commit/711e132711006eb5a63384d8f88716f8b8432616))


### Documentation

* Updated documentation for message NetworkInterface ([711e132](https://github.com/googleapis/python-batch/commit/711e132711006eb5a63384d8f88716f8b8432616))

## [0.6.0](https://github.com/googleapis/python-batch/compare/v0.5.0...v0.6.0) (2022-12-15)


### Features

* Add InstancePolicy.boot_disk ([7e275de](https://github.com/googleapis/python-batch/commit/7e275de7ad29f3f410439469a83969a0b94716b0))


### Bug Fixes

* Removed unused endpoints for IAM methods ([7e275de](https://github.com/googleapis/python-batch/commit/7e275de7ad29f3f410439469a83969a0b94716b0))
* **rest:** Remove unsupported HTTP bindings for IAMPolicy RPCs ([7e275de](https://github.com/googleapis/python-batch/commit/7e275de7ad29f3f410439469a83969a0b94716b0))
* ServiceAccount.scopes is no longer deprecated ([7e275de](https://github.com/googleapis/python-batch/commit/7e275de7ad29f3f410439469a83969a0b94716b0))

## [0.5.0](https://github.com/googleapis/python-batch/compare/v0.4.1...v0.5.0) (2022-12-07)


### Features

* add support for `google.cloud.batch.__version__` ([2f6bdca](https://github.com/googleapis/python-batch/commit/2f6bdcace12b0401e239b08e83a7cb381005d275))
* Add typing to proto.Message based class attributes ([2f6bdca](https://github.com/googleapis/python-batch/commit/2f6bdcace12b0401e239b08e83a7cb381005d275))
* Adds named reservation to InstancePolicy ([9414457](https://github.com/googleapis/python-batch/commit/9414457a16f80cb546b19db1d8f4260883e6f21f))


### Bug Fixes

* Add dict typing for client_options ([2f6bdca](https://github.com/googleapis/python-batch/commit/2f6bdcace12b0401e239b08e83a7cb381005d275))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([1b70819](https://github.com/googleapis/python-batch/commit/1b708191b9dc978930ac38870a994777979f84bf))
* Drop usage of pkg_resources ([1b70819](https://github.com/googleapis/python-batch/commit/1b708191b9dc978930ac38870a994777979f84bf))
* Fix timeout default values ([1b70819](https://github.com/googleapis/python-batch/commit/1b708191b9dc978930ac38870a994777979f84bf))


### Documentation

* Remove "not yet implemented" for Accelerator & Refine Volume API docs ([9414457](https://github.com/googleapis/python-batch/commit/9414457a16f80cb546b19db1d8f4260883e6f21f))
* **samples:** Snippetgen handling of repeated enum field ([2f6bdca](https://github.com/googleapis/python-batch/commit/2f6bdcace12b0401e239b08e83a7cb381005d275))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([1b70819](https://github.com/googleapis/python-batch/commit/1b708191b9dc978930ac38870a994777979f84bf))
* update the job id format requirement ([9414457](https://github.com/googleapis/python-batch/commit/9414457a16f80cb546b19db1d8f4260883e6f21f))

## [0.4.1](https://github.com/googleapis/python-batch/compare/v0.4.0...v0.4.1) (2022-10-27)


### Documentation

* **samples:** Adding code samples for log reading ([#56](https://github.com/googleapis/python-batch/issues/56)) ([9b44e35](https://github.com/googleapis/python-batch/commit/9b44e35f3da228deae8815ba91a0710fea760b2b))

## [0.4.0](https://github.com/googleapis/python-batch/compare/v0.3.2...v0.4.0) (2022-10-18)


### Features

* Enable install_gpu_drivers flag in v1 proto ([e7b8681](https://github.com/googleapis/python-batch/commit/e7b868119425531b402240452af810d706662e80))


### Documentation

* Refine comments for deprecated proto fields ([e7b8681](https://github.com/googleapis/python-batch/commit/e7b868119425531b402240452af810d706662e80))
* Refine comments for deprecated proto fields ([e7b8681](https://github.com/googleapis/python-batch/commit/e7b868119425531b402240452af810d706662e80))
* Refine GPU drivers installation proto description ([e7b8681](https://github.com/googleapis/python-batch/commit/e7b868119425531b402240452af810d706662e80))
* Refine GPU drivers installation proto description ([#57](https://github.com/googleapis/python-batch/issues/57)) ([e7b8681](https://github.com/googleapis/python-batch/commit/e7b868119425531b402240452af810d706662e80))
* Update the API comments about the device_name ([e7b8681](https://github.com/googleapis/python-batch/commit/e7b868119425531b402240452af810d706662e80))
* Update the API comments about the device_name ([e7b8681](https://github.com/googleapis/python-batch/commit/e7b868119425531b402240452af810d706662e80))

## [0.3.2](https://github.com/googleapis/python-batch/compare/v0.3.1...v0.3.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#53](https://github.com/googleapis/python-batch/issues/53)) ([db79e36](https://github.com/googleapis/python-batch/commit/db79e36e9c7193a5b81351b63eb7d4985fc981da))
* **deps:** require google-api-core&gt;=1.33.2 ([db79e36](https://github.com/googleapis/python-batch/commit/db79e36e9c7193a5b81351b63eb7d4985fc981da))

## [0.3.1](https://github.com/googleapis/python-batch/compare/v0.3.0...v0.3.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf &gt;= 3.20.2 ([#47](https://github.com/googleapis/python-batch/issues/47)) ([aa83e55](https://github.com/googleapis/python-batch/commit/aa83e556112d4649a7de59a91ae942830dde4688))


### Documentation

* **samples:** Adding sample for bucket mounting ([#43](https://github.com/googleapis/python-batch/issues/43)) ([af33ed9](https://github.com/googleapis/python-batch/commit/af33ed9ab12e7d72a21dab4f4fefb5f5104d0595))
* **samples:** Adding samples for list and get tasks ([#50](https://github.com/googleapis/python-batch/issues/50)) ([9401da1](https://github.com/googleapis/python-batch/commit/9401da162fcde57dcbf9aff97f289e2cffb3dc9f))
* **samples:** Adding samples for template usage ([#41](https://github.com/googleapis/python-batch/issues/41)) ([7376708](https://github.com/googleapis/python-batch/commit/73767084e1f63e68cb1ade22f390ef208017a6ac))

## [0.3.0](https://github.com/googleapis/python-batch/compare/v0.2.0...v0.3.0) (2022-09-16)


### Features

* Add support for REST transport ([#37](https://github.com/googleapis/python-batch/issues/37)) ([e48b9ba](https://github.com/googleapis/python-batch/commit/e48b9badf426683dc65c8ed3c570a9b5b44a119f))


### Bug Fixes

* **deps:** require google-api-core>=1.33.1,>=2.8.0 ([e48b9ba](https://github.com/googleapis/python-batch/commit/e48b9badf426683dc65c8ed3c570a9b5b44a119f))
* **deps:** require protobuf >= 3.20.1 ([e48b9ba](https://github.com/googleapis/python-batch/commit/e48b9badf426683dc65c8ed3c570a9b5b44a119f))


### Documentation

* **samples:** Adding first sample code + tests ([#22](https://github.com/googleapis/python-batch/issues/22)) ([d8a4864](https://github.com/googleapis/python-batch/commit/d8a4864133ad41e8dec11870ab4a1a9bbbca3292))

## [0.2.0](https://github.com/googleapis/python-batch/compare/v0.1.2...v0.2.0) (2022-08-31)


### Features

* environment variables, disk interfaces ([#19](https://github.com/googleapis/python-batch/issues/19)) ([5ad7d76](https://github.com/googleapis/python-batch/commit/5ad7d76b2c4835798c45ee5168834f22cd691edb))
* generate v1alpha ([#25](https://github.com/googleapis/python-batch/issues/25)) ([6bbff85](https://github.com/googleapis/python-batch/commit/6bbff8560eacd79787c8f4148a43fe116953c4d6))

## [0.1.2](https://github.com/googleapis/python-batch/compare/v0.1.1...v0.1.2) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#12](https://github.com/googleapis/python-batch/issues/12)) ([2e7628d](https://github.com/googleapis/python-batch/commit/2e7628d1830d82217e72b7e4497bac96743bab3e))
* **deps:** require proto-plus >= 1.22.0 ([2e7628d](https://github.com/googleapis/python-batch/commit/2e7628d1830d82217e72b7e4497bac96743bab3e))

## [0.1.1](https://github.com/googleapis/python-batch/compare/v0.1.0...v0.1.1) (2022-07-18)


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#5](https://github.com/googleapis/python-batch/issues/5)) ([2c70ad2](https://github.com/googleapis/python-batch/commit/2c70ad23bc6366178ca8c9c86a1950a283641d9e))

## 0.1.0 (2022-07-08)


### Features

* generate v1 ([3e74724](https://github.com/googleapis/python-batch/commit/3e747247f0a5c7784ef216fccaedddddc45f0768))
