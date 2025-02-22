from pydantic import BaseModel


class Image(BaseModel):
    """Image object"""

    height: int | None
    width: int | None
    url: str


class TracksSummary(BaseModel):
    """TracksSummary object"""

    href: str
    total: int


class OwnerSummary(BaseModel):
    """OwnerSummary object"""

    display_name: str
    external_urls: dict[str, str]
    href: str
    id: str
    type: str
    uri: str


class Playlist(BaseModel):
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


class Playlists(BaseModel):
    """Playlists object"""

    href: str
    items: list[Playlist]
    limit: int
    next: int | str | None
    offset: int
    previous: int | None
    total: int


class AddedBy(BaseModel):
    """Added_by object"""

    external_urls: object
    href: str
    id: str
    type: str
    uri: str


class Artist(BaseModel):
    """Artist object"""

    external_urls: object
    href: str
    id: str
    name: str
    type: str
    uri: str


class Album(BaseModel):
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


class Track(BaseModel):
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
    preview_url: str | None
    track: bool
    track_number: int
    type: str
    uri: str


class TrackItem(BaseModel):
    """TrackItem object"""

    added_at: str
    added_by: AddedBy
    is_local: bool
    primary_color: str | None
    track: Track
    video_thumbnail: object


class Tracks(BaseModel):
    """Tracks object"""

    href: str
    items: list[TrackItem]
    limit: int
    next: int | str | None
    offset: int
    previous: int | None
    total: int
