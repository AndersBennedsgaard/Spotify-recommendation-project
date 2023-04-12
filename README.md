# Spotify recommendation project

Just a simple machine learning project to create a new playlist on Spotify according to similarity to favorite songs

Remember to create `.env` at the root of the project which contains:

```bash
SPOTIPY_CLIENT_ID=<CLIENT_ID>
SPOTIPY_CLIENT_SECRET=<CLIENT_SECRET>
```

Using

* [Spotipy](https://spotipy.readthedocs.io/)

Based on

* [Clustering Music to Create your Playlists on Spotify Using Python and R](https://towardsdatascience.com/clustering-music-to-create-your-personal-playlists-on-spotify-using-python-and-k-means-a39c4158589a)
* [Spotify: Analyzing and Predicting Songs](https://medium.com/mlreview/spotify-analyzing-and-predicting-songs-58827a0fa42b)
* [Making Your Own Spotify Discover Weekly Playlist](https://towardsdatascience.com/making-your-own-discover-weekly-f1ac7546fedb)
* [Build Your Own Spotify Playlist of Best Playlist Recommendations!](https://medium.com/deep-learning-turkey/build-your-own-spotify-playlist-of-best-playlist-recommendations-fc9ebe92826a)
* [How to Create Large Music Datasets Using Spotipy](https://towardsdatascience.com/how-to-create-large-music-datasets-using-spotipy-40e7242cc6a6)

## (Future) usage

```sh
# log in using environment variables / browser?
sr login

# analyse a playlist, show plots, numbers, fancy stuff
sr analyse <source-playlist>

# generate a new playlist with recommendations based on a source playlist
# Analyses the playlist if it hasn't been done
# `--visualize` shows the figures and analytics from `sr analyse`
sr generate <source-playlist> <new-playlist>

# improves a playlist with tracks from `sr generate`
# `--force` bypasses the confirmation 
# `--backup=true` creates a backup of the source playlist
sr improve <source-playlist>
```
