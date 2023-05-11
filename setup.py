from setuptools import setup, find_packages

setup(
    name = 'spotify2midi',
    version = 'beta',
    description = "This package creates MIDI file from Spotify URL using Get Track's Audio Analysis of Spotify Web API.",
    install_requires = ['spotipy', 'numpy', 'mido'],
    packages = find_packages()
)
