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
    )
    for i, col_i in enumerate(column_names):
        for j, col_j in enumerate(column_names):
            axis: plt.Axes = axes[j, i]  # type: ignore
            axis.scatter(data[:, i], data[:, j], s=1, c="tab:blue")
            if secondary_data is not None:
                axis.scatter(
                    secondary_data[:, i], secondary_data[:, j], s=1, c="tab:orange"
                )
            axis.set_xticks([])
            axis.set_xticklabels([])
            axis.set_yticks([])
            axis.set_yticklabels([])
            if i == 0:
                axis.set_ylabel(col_j)
            if j == 0:
                axis.set_xlabel(col_i)
                axis.xaxis.set_label_position("top")

    # Remove white-space between subplots
    plt.subplots_adjust(wspace=0, hspace=0)
    return fig, axes
