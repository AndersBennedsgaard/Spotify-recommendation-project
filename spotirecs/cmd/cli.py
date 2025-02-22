import click


@click.group()
def main():
    """Spotify Recommendation System."""


@main.command()
def login():
    """Log in to Spotify using environment variables / browser?"""
    print("Logging in...")


@main.command()
@click.argument("playlist")
def analyse(playlist: str):
    """Analyse a playlist, show plots, numbers, fancy stuff."""
    print(f"Analyzing playlist {playlist}...")


@main.command()
@click.option(
    "--source-playlist",
    prompt="Source playlist",
    help="The source playlist to analyse.",
)
@click.option(
    "--new-playlist",
    prompt="New playlist",
    help="The new playlist to generate.",
)
@click.option(
    "--visualize",
    help="Show the figures and analytics from `sr analyse`.",
    is_flag=True,
)
def generate(source_playlist: str, new_playlist: str, visualize: bool = False):
    """Generate a new playlist with recommendations based on a source playlist."""
    print(f"Generating a new playlist from {source_playlist} to {new_playlist}...")
    if visualize:
        print("Visualizing...")


@main.command()
@click.argument("playlist")
@click.option("--force", help="Bypass the confirmation.", is_flag=True)
@click.option("--backup", help="Create a backup of the source playlist.", is_flag=True)
def improve(playlist: str, force: bool = False, backup: bool = False):
    """Improve a playlist with tracks from `sr generate`."""
    print(f"Improving playlist {playlist}...")
    if force:
        print("Forcing...")
    if backup:
        print("Creating backup...")
