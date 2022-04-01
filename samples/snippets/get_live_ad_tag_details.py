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

"""Google Cloud Video Stitcher sample for getting the specified ad tag detail for a live session.
Example usage:
    python get_live_ad_tag_details.py --project_number <project-number> --location <location> --session_id <session-id> --ad_tag_details_id <ad-tag-details-id>
"""

# [START video_stitcher_get_live_ad_tag_details]

import argparse

from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
    VideoStitcherServiceClient,
)


def get_live_ad_tag_details(project_number, location, session_id, ad_tag_details_id):
    """Gets the specified ad tag detail for a live session.
    Args:
        project_number: The GCP project number.
        location: The location of the session.
        session_id: The ID of the live session.
        ad_tag_details_id: The id of the ad tag details."""

    client = VideoStitcherServiceClient()

    name = client.live_ad_tag_detail_path(
        project_number, location, session_id, ad_tag_details_id
    )
    response = client.get_live_ad_tag_detail(name=name)
    print(f"Live ad tag details: {response.name}")
    return response


# [END video_stitcher_get_live_ad_tag_details]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_number", help="Your Cloud project number.", required=True
    )
    parser.add_argument(
        "--location", help="The location of the live session.", required=True
    )
    parser.add_argument(
        "--session_id", help="The ID of the live session.", required=True
    )
    parser.add_argument(
        "--ad_tag_details_id", help="The ID of the ad tag details.", required=True
    )
    args = parser.parse_args()
    get_live_ad_tag_details(
        args.project_number, args.location, args.session_id, args.ad_tag_details_id
    )
