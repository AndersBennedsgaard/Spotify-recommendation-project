from typing import TypedDict


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
