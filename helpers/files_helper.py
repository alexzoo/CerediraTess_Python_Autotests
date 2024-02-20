import os
from pathlib import Path


def find_project_root(current_path: Path, marker_file: str = 'config.ini') -> Path:
    """
    Searches for the project root by moving up through the directories until it finds a marker file (e.g., 'config.ini').

    :param current_path: Path, the starting path for the search.
    :param marker_file: str, the name of the marker file.
    :return: Path, the path to the project root.
    """
    current_path = current_path.resolve()
    for parent in current_path.parents:
        if (parent / marker_file).exists():
            return parent
    raise FileNotFoundError(f"Can't find root with marker file: '{marker_file}'.")


def get_dir_path(folder: str) -> Path:
    """
    This function finds the project root directory and creates a directory with the given name if it does not exist.

    :param folder: The name of the directory to create.
    :return: The path to the directory.
    """
    project_root = find_project_root(Path(__file__), marker_file='config.ini')
    dir_path = project_root / folder
    if not dir_path.exists():
        os.makedirs(dir_path)
    return dir_path
