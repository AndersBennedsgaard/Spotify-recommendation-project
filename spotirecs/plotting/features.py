<<<<<<< HEAD
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np


def plot_features(
    column_names: list[str],
    data: np.ndarray,
    secondary_data: Optional[np.ndarray] = None,
):
    """Make a plot of features extracted from a list of tracks in Spotify"""

    if secondary_data is not None and data.shape[1] != secondary_data.shape[1]:
        raise IndexError("Data of different dimensions")

    fig, axes = plt.subplots(
        len(column_names),
        len(column_names),
        figsize=(len(column_names) * 2, len(column_names) * 2),
=======
import matplotlib.pyplot as plt
import pandas as pd


def plot_features(column_names: list[str], data: pd.DataFrame):
    """Make a plot of features extracted from a list of tracks in Spotify"""

    fig, axes = plt.subplots(
        len(column_names), len(column_names), figsize=(len(column_names) * 2, len(column_names) * 2)
>>>>>>> 6deb708 (temporary commit)
    )
    for i, col_i in enumerate(column_names):
        for j, col_j in enumerate(column_names):
            axis: plt.Axes = axes[j, i]  # type: ignore
<<<<<<< HEAD
            axis.scatter(data[:, i], data[:, j], s=1, c="tab:blue")
            if secondary_data is not None:
                axis.scatter(
                    secondary_data[:, i], secondary_data[:, j], s=1, c="tab:orange"
                )
=======
            axis.scatter(
                data.loc[data['rating'] == 1][col_j],
                data.loc[data['rating'] == 1][col_i],
                s=1, c='tab:blue'
            )
            axis.scatter(
                data.loc[data['rating'] == 0][col_j],
                data.loc[data['rating'] == 0][col_i],
                s=1, c='tab:orange'
            )
>>>>>>> 6deb708 (temporary commit)
            axis.set_xticks([])
            axis.set_xticklabels([])
            axis.set_yticks([])
            axis.set_yticklabels([])
            if i == 0:
                axis.set_ylabel(col_j)
            if j == 0:
                axis.set_xlabel(col_i)
<<<<<<< HEAD
                axis.xaxis.set_label_position("top")
=======
                axis.xaxis.set_label_position('top')
>>>>>>> 6deb708 (temporary commit)

    # Remove white-space between subplots
    plt.subplots_adjust(wspace=0, hspace=0)
    return fig, axes
