import spotipy

from spotirecs.models import Playlist, Tracks


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
