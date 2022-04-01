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

"""Google Cloud Video Stitcher sample for listing the stitch details for a video on demand (VOD) session.
Example usage:
    python list_vod_stitch_details.py --project_number <project-number> --location <location> --session_id <session-id>
"""

# [START video_stitcher_list_vod_stitch_details]

import argparse

from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
    VideoStitcherServiceClient,
)


def list_vod_stitch_details(project_number, location, session_id):
    """Lists the stitch details for the specified VOD session.
    Args:
        project_number: The GCP project number.
        location: The location of the session.
        session_id: The ID of the VOD session."""

    client = VideoStitcherServiceClient()

    parent = client.vod_session_path(project_number, location, session_id)
    page_result = client.list_vod_stitch_details(parent=parent)
    for response in page_result:
        print(response)

    return response


# [END video_stitcher_list_vod_stitch_details]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_number", help="Your Cloud project number.", required=True
    )
    parser.add_argument(
        "--location", help="The location of the VOD session.", required=True
    )
    parser.add_argument(
        "--session_id", help="The ID of the VOD session.", required=True
    )
    args = parser.parse_args()
    list_vod_stitch_details(args.project_number, args.location, args.session_id)
