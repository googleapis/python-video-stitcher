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

"""Google Cloud Video Stitcher sample for getting a livestream session.
Example usage:
    python get_live_session.py --project_number <project-number> --location <location> --session_id <session-id>
"""

# [START video_stitcher_get_live_session]

import argparse

from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
    VideoStitcherServiceClient,
)


def get_live_session(project_number, location, session_id):
    """Gets a live session. Live sessions are ephemeral resources that expire after a few minutes.
    Args:
        project_number: The GCP project number.
        location: The location of the session.
        session_id: The ID of the live session."""

    client = VideoStitcherServiceClient()

    name = client.live_session_path(project_number, location, session_id)
    response = client.get_live_session(name=name)
    print(f"Live session: {response.name}")
    return response


# [END video_stitcher_get_live_session]

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
    args = parser.parse_args()
    get_live_session(args.project_number, args.location, args.session_id)
