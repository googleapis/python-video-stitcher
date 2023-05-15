# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

from google.protobuf import duration_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.video.stitcher_v1.types import companions, events, live_configs

__protobuf__ = proto.module(
    package="google.cloud.video.stitcher.v1",
    manifest={
        "VodSession",
        "Interstitials",
        "VodSessionAd",
        "VodSessionContent",
        "VodSessionAdBreak",
        "LiveSession",
        "ManifestOptions",
        "RenditionFilter",
    },
)


class VodSession(proto.Message):
    r"""Metadata for a VOD session. The session expires 4 hours after
    its creation.

    Attributes:
        name (str):
            Output only. The name of the VOD session, in the form of
            ``projects/{project_number}/locations/{location}/vodSessions/{id}``.
        interstitials (google.cloud.video.stitcher_v1.types.Interstitials):
            Output only. Metadata of what was stitched
            into the content.
        play_uri (str):
            Output only. The playback URI of the stitched
            content.
        source_uri (str):
            Required. URI of the media to stitch.
        ad_tag_uri (str):
            Required. Ad tag URI.
        ad_tag_macro_map (MutableMapping[str, str]):
            Key value pairs for ad tag macro replacement. If the
            specified ad tag URI has macros, this field provides the
            mapping to the value that will replace the macro in the ad
            tag URI. Macros are designated by square brackets. For
            example:

            Ad tag URI:
            ``"https://doubleclick.google.com/ad/1?geo_id=[geoId]"``

            Ad tag macro map: ``{"geoId": "123"}``

            Fully qualified ad tag:
            ``"``\ https://doubleclick.google.com/ad/1?geo_id=123"\`
        manifest_options (google.cloud.video.stitcher_v1.types.ManifestOptions):
            Additional options that affect the output of
            the manifest.
        asset_id (str):
            Output only. The generated ID of the
            VodSession's source media.
        ad_tracking (google.cloud.video.stitcher_v1.types.AdTracking):
            Required. Determines how the ad should be tracked. If
            [gam_vod_config][google.cloud.video.stitcher.v1.VodSession.gam_vod_config]
            is set, the value must be ``CLIENT`` because the IMA SDK
            handles ad tracking.
        gam_settings (google.cloud.video.stitcher_v1.types.VodSession.GamSettings):
            This field should be set with appropriate
            values if GAM is being used for ads.
    """

    class GamSettings(proto.Message):
        r"""Defines fields related to Google Ad Manager (GAM). This
        should be set if GAM is being used for ads.

        Attributes:
            network_code (str):
                Required. Ad Manager network code.
            stream_id (str):
                Required. The stream ID generated by Ad
                Manager.
        """

        network_code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        stream_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    interstitials: "Interstitials" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Interstitials",
    )
    play_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    source_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ad_tag_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ad_tag_macro_map: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    manifest_options: "ManifestOptions" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ManifestOptions",
    )
    asset_id: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ad_tracking: live_configs.AdTracking = proto.Field(
        proto.ENUM,
        number=11,
        enum=live_configs.AdTracking,
    )
    gam_settings: GamSettings = proto.Field(
        proto.MESSAGE,
        number=13,
        message=GamSettings,
    )


class Interstitials(proto.Message):
    r"""Describes what was stitched into a VOD session's manifest.

    Attributes:
        ad_breaks (MutableSequence[google.cloud.video.stitcher_v1.types.VodSessionAdBreak]):
            List of ad breaks ordered by time.
        session_content (google.cloud.video.stitcher_v1.types.VodSessionContent):
            Information related to the content of the VOD
            session.
    """

    ad_breaks: MutableSequence["VodSessionAdBreak"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="VodSessionAdBreak",
    )
    session_content: "VodSessionContent" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="VodSessionContent",
    )


class VodSessionAd(proto.Message):
    r"""Metadata for an inserted ad in a VOD session.

    Attributes:
        duration (google.protobuf.duration_pb2.Duration):
            Duration in seconds of the ad.
        companion_ads (google.cloud.video.stitcher_v1.types.CompanionAds):
            Metadata of companion ads associated with the
            ad.
        activity_events (MutableSequence[google.cloud.video.stitcher_v1.types.Event]):
            The list of progress tracking events for the ad break. These
            can be of the following IAB types: ``MUTE``, ``UNMUTE``,
            ``PAUSE``, ``CLICK``, ``CLICK_THROUGH``, ``REWIND``,
            ``RESUME``, ``ERROR``, ``FULLSCREEN``, ``EXIT_FULLSCREEN``,
            ``EXPAND``, ``COLLAPSE``, ``ACCEPT_INVITATION_LINEAR``,
            ``CLOSE_LINEAR``, ``SKIP``.
    """

    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    companion_ads: companions.CompanionAds = proto.Field(
        proto.MESSAGE,
        number=2,
        message=companions.CompanionAds,
    )
    activity_events: MutableSequence[events.Event] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=events.Event,
    )


class VodSessionContent(proto.Message):
    r"""Metadata for the entire stitched content in a VOD session.

    Attributes:
        duration (google.protobuf.duration_pb2.Duration):
            The total duration in seconds of the content
            including the ads stitched in.
    """

    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class VodSessionAdBreak(proto.Message):
    r"""Metadata for an inserted ad break.

    Attributes:
        progress_events (MutableSequence[google.cloud.video.stitcher_v1.types.ProgressEvent]):
            List of events that are expected to be
            triggered, ordered by time.
        ads (MutableSequence[google.cloud.video.stitcher_v1.types.VodSessionAd]):
            Ordered list of ads stitched into the ad
            break.
        end_time_offset (google.protobuf.duration_pb2.Duration):
            Ad break end time in seconds relative to the
            start of the VOD asset.
        start_time_offset (google.protobuf.duration_pb2.Duration):
            Ad break start time in seconds relative to
            the start of the VOD asset.
    """

    progress_events: MutableSequence[events.ProgressEvent] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=events.ProgressEvent,
    )
    ads: MutableSequence["VodSessionAd"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="VodSessionAd",
    )
    end_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    start_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )


class LiveSession(proto.Message):
    r"""Metadata for a live session. The session expires 5 minutes
    after the client stops fetching the session's playlists.

    Attributes:
        name (str):
            Output only. The name of the live session, in the form of
            ``projects/{project}/locations/{location}/liveSessions/{id}``.
        play_uri (str):
            Output only. The URI to play the live
            session's ad-stitched stream.
        ad_tag_macros (MutableMapping[str, str]):
            Key value pairs for ad tag macro replacement. If the
            specified ad tag URI has macros, this field provides the
            mapping to the value that will replace the macro in the ad
            tag URI. Macros are designated by square brackets.

            For example:

            Ad tag URI:
            "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

            Ad tag macros: ``{"geoId": "123"}``

            Fully qualified ad tag:
            ``"https://doubleclick.google.com/ad/1?geo_id=123"``
        manifest_options (google.cloud.video.stitcher_v1.types.ManifestOptions):
            Additional options that affect the output of
            the manifest.
        gam_settings (google.cloud.video.stitcher_v1.types.LiveSession.GamSettings):
            This field should be set with appropriate
            values if GAM is being used for ads.
        live_config (str):
            Required. The resource name of the live config for this
            session, in the form of
            ``projects/{project}/locations/{location}/liveConfigs/{id}``.
    """

    class GamSettings(proto.Message):
        r"""Defines fields related to Google Ad Manager (GAM). This
        should be set if GAM
        is being used for ads.

        Attributes:
            stream_id (str):
                Required. The stream ID generated by Ad
                Manager.
        """

        stream_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    play_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ad_tag_macros: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    manifest_options: "ManifestOptions" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="ManifestOptions",
    )
    gam_settings: GamSettings = proto.Field(
        proto.MESSAGE,
        number=15,
        message=GamSettings,
    )
    live_config: str = proto.Field(
        proto.STRING,
        number=16,
    )


class ManifestOptions(proto.Message):
    r"""Options for manifest generation.

    Attributes:
        include_renditions (MutableSequence[google.cloud.video.stitcher_v1.types.RenditionFilter]):
            If specified, the output manifest will only
            return renditions matching the specified
            filters.
        bitrate_order (google.cloud.video.stitcher_v1.types.ManifestOptions.OrderPolicy):
            If specified, the output manifest will orders
            the video and muxed renditions by bitrate
            according to the ordering policy.
    """

    class OrderPolicy(proto.Enum):
        r"""Defines the ordering policy during manifest generation.

        Values:
            ORDER_POLICY_UNSPECIFIED (0):
                Ordering policy is not specified.
            ASCENDING (1):
                Order by ascending.
            DESCENDING (2):
                Order by descending.
        """
        ORDER_POLICY_UNSPECIFIED = 0
        ASCENDING = 1
        DESCENDING = 2

    include_renditions: MutableSequence["RenditionFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RenditionFilter",
    )
    bitrate_order: OrderPolicy = proto.Field(
        proto.ENUM,
        number=2,
        enum=OrderPolicy,
    )


class RenditionFilter(proto.Message):
    r"""Filters for a video or muxed redition.

    Attributes:
        bitrate_bps (int):
            Bitrate in bits per second for the rendition.
            If set, only renditions with the exact bitrate
            will match.
        codecs (str):
            Codecs for the rendition. If set, only
            renditions with the exact value will match.
    """

    bitrate_bps: int = proto.Field(
        proto.INT32,
        number=1,
    )
    codecs: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
