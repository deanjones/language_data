"""
Used for locating a file in the data directory.
"""
from importlib import resources
from pathlib import Path


def data_filename(filename):
    """
    Given a relative filename, get the full path to that file in the data
    directory.
    """
    data_root = resources.files('language_data') / 'data'
    with resources.as_file(data_root) as path:
        return Path(path) / filename
