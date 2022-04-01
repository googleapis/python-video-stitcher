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

"""Google Cloud Video Stitcher sample for deleting a slate.
Example usage:
    python delete_slate.py --project_number <project-number> --location <location> --slate_id <slate-id>
"""

# [START video_stitcher_delete_slate]

import argparse

from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
    VideoStitcherServiceClient,
)


def delete_slate(project_number, location, slate_id):
    """Deletes a slate.
    Args:
        project_number: The GCP project number.
        location: The location of the slate.
        slate_id: The user-defined slate ID."""

    client = VideoStitcherServiceClient()

    name = f"projects/{project_number}/locations/{location}/slates/{slate_id}"
    response = client.delete_slate(name=name)
    print("Deleted slate")
    return response


# [END video_stitcher_delete_slate]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_number", help="Your Cloud project number.", required=True
    )
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
    delete_slate(
        args.project_number,
        args.location,
        args.slate_id,
    )
