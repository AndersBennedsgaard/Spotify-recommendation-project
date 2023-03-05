from setuptools import setup, find_packages


with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("LICENSE", encoding="utf-8") as f:
    lic = f.read()

required_packages = [
    "numpy",
    "pandas",
    "requests",
    "spotipy",
    "scikit-learn",
    "matplotlib",
]


extras_packages = {
    'docs': [],
    'dev': [
        "pylint",
        "pytest",
        "flake8",
        "ipykernel",
        "jupyter",
        "pipreqs"
        # "black>=22.0.0",
    ]
}

setup(
    name="spotirecs",
    version="0.1.0",
    description="Spotify Recommendations",
    author="Anders Bennedsgaard",
    author_email="abbennedsgaard@gmail.com",
    url="https://github.com/AndersBennedsgaard/Spotify-recommendation-project",
    license=lic,
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(where="."),
    install_requires=required_packages,
    extras_require=extras_packages
)
