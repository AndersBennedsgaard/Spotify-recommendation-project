import spotipy

from spotirecs.models import Playlist, Playlists, Tracks


def get_playlists(spotify: spotipy.Spotify, username_id: str) -> Playlists:
    """Get all user playlists"""
    playlists: dict | None = spotify.user_playlists(username_id)
    if playlists is None:
        raise ValueError("Playlists could not be retrieved")

    return Playlists(**playlists)


def get_playlist_tracks(spotify: spotipy.Spotify, playlist: Playlist) -> tuple[list[str], list[str]]:
    """Get tracks in a Spotify playlist"""
    track_ids: list[str] = []
    track_names: list[str] = []

    for i in range(0, playlist.tracks.total, 100):
        track_results_dict: dict | None = spotify.user_playlist_tracks(
            playlist.owner.id, playlist.id, offset=i, limit=100
        )

        if track_results_dict is None:
            print("No tracks in user playlist")
            break

        track_results = Tracks(**track_results_dict)

        # TODO: return track objects instead of IDs
        for track in track_results.items:
            track_ids.append(track.track.id)
            track_names.append(track.track.name)

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
