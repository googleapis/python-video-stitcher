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

"""Google Cloud Video Stitcher sample for creating a Media CDN key
or a Cloud CDN key. A CDN key is used to retrieve protected media.
Example usage:
    python create_cdn_key.py --project_id <project-id> --location <location> \
        --cdn_key_id <cdn_key_id> --hostname <hostname> \
        --key_name <name> --private_key <key> [--is_cloud_cdn]
"""

# [START videostitcher_create_cdn_key]

import argparse

from google.cloud.video import stitcher_v1
from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
    VideoStitcherServiceClient,
)


def create_cdn_key(
    project_id: str,
    location: str,
    cdn_key_id: str,
    hostname: str,
    key_name: str,
    private_key: str,
    is_cloud_cdn: bool,
) -> str:
    """Creates a Cloud CDN or Media CDN key.
    Args:
        project_id: The GCP project ID.
        location: The location in which to create the CDN key.
        cdn_key_id: The user-defined CDN key ID.
        hostname: The hostname to which this CDN key applies.
        key_name: For a Media CDN key, this is the keyset name.
                  For a Cloud CDN key, this is the public name of the CDN key.
        private_key: For a Media CDN key, this is a 64-byte Ed25519 private
                     key encoded as a base64-encoded string.
                     See https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn
                     for more information. For a Cloud CDN key, this is a base64-encoded string secret.
        is_cloud_cdn: If true, create a Cloud CDN key. If false, create a Media CDN key."""

    client = VideoStitcherServiceClient()

    parent = f"projects/{project_id}/locations/{location}"

    cdn_key = stitcher_v1.types.CdnKey(
        name=cdn_key_id,
        hostname=hostname,
    )

    if is_cloud_cdn:
        cdn_key.google_cdn_key = stitcher_v1.types.GoogleCdnKey(
            key_name=key_name,
            private_key=private_key,
        )
    else:
        cdn_key.media_cdn_key = stitcher_v1.types.MediaCdnKey(
            key_name=key_name,
            private_key=private_key,
        )

    operation = client.create_cdn_key(
        parent=parent, cdn_key_id=cdn_key_id, cdn_key=cdn_key
    )
    response = operation.result(600)
    print(f"CDN key: {response.name}")
    return response


# [END videostitcher_create_cdn_key]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_id", help="Your Cloud project ID.", required=True)
    parser.add_argument(
        "--location",
        help="The location in which to create the CDN key.",
        default="us-central1",
    )
    parser.add_argument(
        "--cdn_key_id",
        help="The user-defined CDN key ID.",
        required=True,
    )
    parser.add_argument(
        "--hostname",
        help="The hostname to which this CDN key applies.",
        required=True,
    )
    parser.add_argument(
        "--key_name",
        help="For a Media CDN key, this is the keyset name. For a Cloud CDN"
        + " key, this is the public name of the CDN key.",
        required=True,
    )
    parser.add_argument(
        "--private_key",
        help="For a Media CDN key, this is a 64-byte Ed25519 private key"
        + "encoded as a base64-encoded string. See"
        + " https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn"
        + " for more information. For a Cloud CDN key, this is a"
        + " base64-encoded string secret.",
        required=True,
    )
    parser.add_argument(
        "--is_cloud_cdn",
        action="store_true",
        help="If included, create a Cloud CDN key. If absent, create a Media CDN key.",
    )
    args = parser.parse_args()
    create_cdn_key(
        args.project_id,
        args.location,
        args.cdn_key_id,
        args.hostname,
        args.key_name,
        args.private_key,
        args.is_cloud_cdn,
    )
