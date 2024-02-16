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


def get_log_dir_path() -> Path:
    """
    This function finds the root directory of the project by searching upwards from the current file path until
    it finds a file with the given marker file name.
    Then it creates a directory called "logs" in that directory if it does not exist.
    Finally, it returns the path to the "logs" directory.

    :return: Path, the path to the "logs" directory.
    """
    project_root = find_project_root(Path(__file__), marker_file='config.ini')
    log_dir_path = project_root / 'logs'
    if not log_dir_path.exists():
        os.makedirs(log_dir_path)
    return log_dir_path
