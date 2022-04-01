#!/usr/bin/env python

# Copyright 2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Video Stitcher sample for listing all slates in a location.
Example usage:
    python list_slates.py --project_number <project-number> --location <location>
"""

# [START video_stitcher_list_slates]

import argparse

from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
    VideoStitcherServiceClient,
)


def list_slates(project_number, location):
    """Lists all slates in a location.
    Args:
        project_number: The GCP project number.
        location: The location of the slates."""

    client = VideoStitcherServiceClient()

    parent = f"projects/{project_number}/locations/{location}"
    response = client.list_slates(parent=parent)
    print("Slates:")
    for slate in response.slates:
        print({slate.name})

    return response


# [END video_stitcher_list_slates]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_number", help="Your Cloud project number.", required=True
    )
    parser.add_argument(
        "--location",
        help="The location of the slates.",
        required=True,
    )
    args = parser.parse_args()
    list_slates(
        args.project_number,
        args.location,
    )
