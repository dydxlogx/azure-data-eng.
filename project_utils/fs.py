"""File-system helpers for project setup."""

from pathlib import Path
from typing import Iterable, List


def ensure_project_dirs(base_dir: Path, directories: Iterable[str]) -> List[Path]:
    """Create project directories if they do not exist.

    Args:
        base_dir: Root directory where subdirectories should be created.
        directories: Directory names (or nested relative paths) to create.

    Returns:
        List of full `Path` objects that were ensured.
    """
    created_paths: List[Path] = []
    base_dir.mkdir(parents=True, exist_ok=True)

    for directory in directories:
        path = base_dir / directory
        path.mkdir(parents=True, exist_ok=True)
        created_paths.append(path)

    return created_paths
