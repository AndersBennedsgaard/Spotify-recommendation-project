from typing import TypedDict

import spotipy


class Image(TypedDict):
    """Image object"""

    height: int
    width: int
    url: str


class TracksSummary(TypedDict):
    """TracksSummary object"""

    href: str
    total: int


class OwnerSummary(TypedDict):
    """OwnerSummary object"""

    display_name: str
    external_urls: dict[str, str]
    href: str
    id: str
    type: str
    uri: str


class Playlist(TypedDict):
    """Playlist object"""

    collaborative: bool
    description: str
    external_urls: dict[str, str]
    href: str
    id: str
    images: list[Image]
    name: str
    owner: OwnerSummary
    primary_color: str | None
    public: bool
    snapshot_id: str
    tracks: TracksSummary
    type: str
    uri: str


class Playlists(TypedDict):
    """Playlists object"""

    href: str
    items: list[Playlist]
    limit: int
    next: int | None
    offset: int
    previous: int | None
    total: int


class AddedBy(TypedDict):
    """Added_by object"""

    external_urls: object
    href: str
    id: str
    type: str
    uri: str


class Artist(TypedDict):
    """Artist object"""

    external_urls: object
    href: str
    id: str
    name: str
    type: str
    uri: str


class Album(TypedDict):
    """Album object"""

    album_type: str
    artists: list[Artist]
    available_markets: list[str]
    external_urls: object
    href: str
    id: str
    images: list[Image]
    name: str
    release_date: str
    release_date_precision: str
    total_tracks: int
    type: str
    uri: str


class Track(TypedDict):
    """Track object"""

    album: Album
    artists: list[Artist]
    available_markets: list[str]
    disc_number: int
    duration_ms: int
    episode: bool
    explicit: bool
    external_ids: object
    external_urls: object
    href: str
    id: str
    is_local: bool
    name: str
    popularity: int
    preview_url: str
    track: bool
    track_number: int
    type: str
    uri: str


class TrackItem(TypedDict):
    """TrackItem object"""

    added_at: str
    added_by: AddedBy
    is_local: bool
    primary_color: str | None
    track: Track
    video_thumbnail: object


class Tracks(TypedDict):
    """Tracks object"""

    href: str
    items: list[TrackItem]
    limit: int
    next: int | None
    offset: int
    previous: int | None
    total: int


def get_playlist_tracks(spotify: spotipy.Spotify, playlist: Playlist):
    """Get tracks in a Spotify playlist"""
    track_ids = []
    track_names = []

    for i in range(0, playlist["tracks"]["total"], 100):
        track_results: Tracks | None = spotify.user_playlist_tracks(
            playlist["owner"]["id"], playlist["id"], offset=i, limit=100
        )
        if track_results is None:
            continue
        for track in track_results["items"]:
            track_ids.append(track["track"]["id"])
            track_names.append(track["track"]["name"])

    return track_ids, track_names


def get_features(spotify: spotipy.Spotify, track_ids: list[str]):
    """Get collective features of a list of tracks"""
    features = []

    for track_id in track_ids:
        feats = spotify.audio_features(track_id)
        if feats is None:
            continue
        for track in feats:
            features.append(track)

    return features
