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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
import pkg_resources

from google.cloud.video.stitcher_v1.types import (
    ad_tag_details,
    cdn_keys,
    sessions,
    slates,
    stitch_details,
    video_stitcher_service,
)

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-video-stitcher",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class VideoStitcherServiceTransport(abc.ABC):
    """Abstract transport class for VideoStitcherService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "videostitcher.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )
        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_cdn_key: gapic_v1.method.wrap_method(
                self.create_cdn_key,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_cdn_keys: gapic_v1.method.wrap_method(
                self.list_cdn_keys,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_cdn_key: gapic_v1.method.wrap_method(
                self.get_cdn_key,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_cdn_key: gapic_v1.method.wrap_method(
                self.delete_cdn_key,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_cdn_key: gapic_v1.method.wrap_method(
                self.update_cdn_key,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_vod_session: gapic_v1.method.wrap_method(
                self.create_vod_session,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_vod_session: gapic_v1.method.wrap_method(
                self.get_vod_session,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_vod_stitch_details: gapic_v1.method.wrap_method(
                self.list_vod_stitch_details,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_vod_stitch_detail: gapic_v1.method.wrap_method(
                self.get_vod_stitch_detail,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_vod_ad_tag_details: gapic_v1.method.wrap_method(
                self.list_vod_ad_tag_details,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_vod_ad_tag_detail: gapic_v1.method.wrap_method(
                self.get_vod_ad_tag_detail,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_live_ad_tag_details: gapic_v1.method.wrap_method(
                self.list_live_ad_tag_details,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_live_ad_tag_detail: gapic_v1.method.wrap_method(
                self.get_live_ad_tag_detail,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_slate: gapic_v1.method.wrap_method(
                self.create_slate,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_slates: gapic_v1.method.wrap_method(
                self.list_slates,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_slate: gapic_v1.method.wrap_method(
                self.get_slate,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_slate: gapic_v1.method.wrap_method(
                self.update_slate,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_slate: gapic_v1.method.wrap_method(
                self.delete_slate,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_live_session: gapic_v1.method.wrap_method(
                self.create_live_session,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_live_session: gapic_v1.method.wrap_method(
                self.get_live_session,
                default_timeout=60.0,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def create_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateCdnKeyRequest],
        Union[cdn_keys.CdnKey, Awaitable[cdn_keys.CdnKey]],
    ]:
        raise NotImplementedError()

    @property
    def list_cdn_keys(
        self,
    ) -> Callable[
        [video_stitcher_service.ListCdnKeysRequest],
        Union[
            video_stitcher_service.ListCdnKeysResponse,
            Awaitable[video_stitcher_service.ListCdnKeysResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.GetCdnKeyRequest],
        Union[cdn_keys.CdnKey, Awaitable[cdn_keys.CdnKey]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteCdnKeyRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateCdnKeyRequest],
        Union[cdn_keys.CdnKey, Awaitable[cdn_keys.CdnKey]],
    ]:
        raise NotImplementedError()

    @property
    def create_vod_session(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateVodSessionRequest],
        Union[sessions.VodSession, Awaitable[sessions.VodSession]],
    ]:
        raise NotImplementedError()

    @property
    def get_vod_session(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodSessionRequest],
        Union[sessions.VodSession, Awaitable[sessions.VodSession]],
    ]:
        raise NotImplementedError()

    @property
    def list_vod_stitch_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodStitchDetailsRequest],
        Union[
            video_stitcher_service.ListVodStitchDetailsResponse,
            Awaitable[video_stitcher_service.ListVodStitchDetailsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_vod_stitch_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodStitchDetailRequest],
        Union[
            stitch_details.VodStitchDetail, Awaitable[stitch_details.VodStitchDetail]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_vod_ad_tag_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodAdTagDetailsRequest],
        Union[
            video_stitcher_service.ListVodAdTagDetailsResponse,
            Awaitable[video_stitcher_service.ListVodAdTagDetailsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_vod_ad_tag_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodAdTagDetailRequest],
        Union[ad_tag_details.VodAdTagDetail, Awaitable[ad_tag_details.VodAdTagDetail]],
    ]:
        raise NotImplementedError()

    @property
    def list_live_ad_tag_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListLiveAdTagDetailsRequest],
        Union[
            video_stitcher_service.ListLiveAdTagDetailsResponse,
            Awaitable[video_stitcher_service.ListLiveAdTagDetailsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_live_ad_tag_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveAdTagDetailRequest],
        Union[
            ad_tag_details.LiveAdTagDetail, Awaitable[ad_tag_details.LiveAdTagDetail]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateSlateRequest],
        Union[slates.Slate, Awaitable[slates.Slate]],
    ]:
        raise NotImplementedError()

    @property
    def list_slates(
        self,
    ) -> Callable[
        [video_stitcher_service.ListSlatesRequest],
        Union[
            video_stitcher_service.ListSlatesResponse,
            Awaitable[video_stitcher_service.ListSlatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.GetSlateRequest],
        Union[slates.Slate, Awaitable[slates.Slate]],
    ]:
        raise NotImplementedError()

    @property
    def update_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateSlateRequest],
        Union[slates.Slate, Awaitable[slates.Slate]],
    ]:
        raise NotImplementedError()

    @property
    def delete_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteSlateRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_live_session(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateLiveSessionRequest],
        Union[sessions.LiveSession, Awaitable[sessions.LiveSession]],
    ]:
        raise NotImplementedError()

    @property
    def get_live_session(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveSessionRequest],
        Union[sessions.LiveSession, Awaitable[sessions.LiveSession]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("VideoStitcherServiceTransport",)
