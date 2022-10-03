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

"""Google Cloud Video Stitcher sample for getting the specified ad tag detail
for a video on demand (VOD) session.
Example usage:
    python get_vod_ad_tag_detail.py --project_id <project-id> --location <location> --session_id <session-id> --ad_tag_details_id <ad-tag-details-id>
"""

# [START videostitcher_get_vod_ad_tag_detail]

import argparse

from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
    VideoStitcherServiceClient,
)


def get_vod_ad_tag_detail(
    project_id: str, location: str, session_id: str, ad_tag_detail_id: str
) -> str:
    """Gets the specified ad tag detail for a VOD session.
    Args:
        project_id: The GCP project ID.
        location: The location of the session.
        session_id: The ID of the VOD session.
        ad_tag_detail_id: The ID of the ad tag details."""

    client = VideoStitcherServiceClient()

    name = client.vod_ad_tag_detail_path(
        project_id, location, session_id, ad_tag_detail_id
    )
    response = client.get_vod_ad_tag_detail(name=name)
    print(f"VOD ad tag detail: {response.name}")
    return response


# [END videostitcher_get_vod_ad_tag_detail]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_id", help="Your Cloud project ID.", required=True)
    parser.add_argument(
        "--location", help="The location of the VOD session.", required=True
    )
    parser.add_argument(
        "--session_id", help="The ID of the VOD session.", required=True
    )
    parser.add_argument(
        "--ad_tag_detail_id", help="The ID of the ad tag details.", required=True
    )
    args = parser.parse_args()
    get_vod_ad_tag_detail(
        args.project_id, args.location, args.session_id, args.ad_tag_detail_id
    )
