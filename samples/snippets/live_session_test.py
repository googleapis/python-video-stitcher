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

import os
import uuid

from google.api_core.exceptions import NotFound

import create_live_session
import create_slate
import delete_slate
import get_live_session
import list_live_ad_tag_details


project_number = os.environ["GOOGLE_CLOUD_PROJECT_NUMBER"]
location = "us-central1"
input_bucket_name = "cloud-samples-data/media/"
input_video_file_name = "hls-live/manifest.m3u8"
live_stream_uri = (
    f"https://storage.googleapis.com/{input_bucket_name}{input_video_file_name}"
)
# Single Inline Linear (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags)
ad_tag_uri = "https://pubads.g.doubleclick.net/gampad/ads?iu=/21775744923/external/single_ad_samples&sz=640x480&cust_params=sample_ct%3Dlinear&ciu_szs=300x250%2C728x90&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator="
slate_id = f"my-python-test-slate-{uuid.uuid4()}"
slate_video_file_name = "ForBiggerJoyrides.mp4"
slate_uri = f"gs://{input_bucket_name}{slate_video_file_name}"


def test_live_session_operations(capsys):

    # Test setup

    slate_name = f"projects/{project_number}/locations/{location}/slates/{slate_id}"

    try:
        delete_slate.delete_slate(project_number, location, slate_id)
    except NotFound as e:
        print(f"Ignoring NotFound, details: {e}")
    out, _ = capsys.readouterr()

    create_slate.create_slate(project_number, location, slate_id, slate_uri)
    out, _ = capsys.readouterr()
    assert slate_name in out

    # Tests

    create_live_session.create_live_session(
        project_number, location, live_stream_uri, ad_tag_uri, slate_id
    )
    out, _ = capsys.readouterr()
    session_name_prefix = (
        f"projects/{project_number}/locations/{location}/liveSessions/"
    )
    assert session_name_prefix in out

    str_slice = out.split("/")
    session_id = str_slice[len(str_slice) - 1].rstrip("\n")
    session_name = (
        f"projects/{project_number}/locations/{location}/liveSessions/{session_id}"
    )
    assert session_name in out

    get_live_session.get_live_session(project_number, location, session_id)
    out, _ = capsys.readouterr()
    assert session_name in out

    # Clean up slate as it is no longer needed

    delete_slate.delete_slate(project_number, location, slate_id)
    out, _ = capsys.readouterr()
    assert "Deleted slate" in out

    # No list or delete methods for live sessions

    # Ad tag details

    list_live_ad_tag_details.list_live_ad_tag_details(
        project_number, location, session_id
    )
    out, _ = capsys.readouterr()
    # Until we have a test livestream to use, nothing is returned (this is {} for the associated REST call).
    # Can't test get_live_ad_tag_details until something is returned.
    # ad_tag_details_name_prefix = f"projects/{project_number}/locations/{location}/liveSessions/{session_id}/liveAdTagDetails/"
    assert "" in out

    # str_slice = response.name.split("/")
    # ad_tag_details_id = str_slice[len(str_slice) - 1].rstrip("\n")
    # ad_tag_details_name = f"projects/{project_number}/locations/{location}/liveSessions/{session_id}/liveAdTagDetails/{ad_tag_details_id}"
    # assert ad_tag_details_name in out

    # get_live_ad_tag_details.get_live_ad_tag_details(project_number, location, session_id, ad_tag_details_id)
    # out, _ = capsys.readouterr()
    # assert ad_tag_details_name in out
