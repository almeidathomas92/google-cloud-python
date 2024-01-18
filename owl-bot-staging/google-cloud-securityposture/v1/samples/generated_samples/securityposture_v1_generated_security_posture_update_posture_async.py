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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdatePosture
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-securityposture


# [START securityposture_v1_generated_SecurityPosture_UpdatePosture_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import securityposture_v1


async def sample_update_posture():
    # Create a client
    client = securityposture_v1.SecurityPostureAsyncClient()

    # Initialize request argument(s)
    posture = securityposture_v1.Posture()
    posture.name = "name_value"
    posture.state = "ACTIVE"
    posture.policy_sets.policy_set_id = "policy_set_id_value"
    posture.policy_sets.policies.policy_id = "policy_id_value"
    posture.policy_sets.policies.constraint.security_health_analytics_module.module_name = "module_name_value"

    request = securityposture_v1.UpdatePostureRequest(
        posture=posture,
        revision_id="revision_id_value",
    )

    # Make the request
    operation = client.update_posture(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END securityposture_v1_generated_SecurityPosture_UpdatePosture_async]
