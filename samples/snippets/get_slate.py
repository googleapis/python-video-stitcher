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

"""Google Cloud Video Stitcher sample for getting a slate.
Example usage:
    python get_slate.py --project_id <project-id> --location <location> \
        --slate_id <slate-id>
"""

# [START videostitcher_get_slate]

import argparse

from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
    VideoStitcherServiceClient,
)


def get_slate(project_id: str, location: str, slate_id: str) -> str:
    """Gets a slate.
    Args:
        project_id: The GCP project ID.
        location: The location of the slate.
        slate_id: The user-defined slate ID."""

    client = VideoStitcherServiceClient()

    name = f"projects/{project_id}/locations/{location}/slates/{slate_id}"
    response = client.get_slate(name=name)
    print(f"Slate: {response.name}")
    return response


# [END videostitcher_get_slate]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_id", help="Your Cloud project ID.", required=True)
    parser.add_argument(
        "--location",
        help="The location of the slate.",
        required=True,
    )
    parser.add_argument(
        "--slate_id",
        help="The user-defined slate ID.",
        required=True,
    )
    args = parser.parse_args()
    get_slate(
        args.project_id,
        args.location,
        args.slate_id,
    )
