"""Command-line interface for make_project."""

import argparse
import sys
from pathlib import Path

SUBDIRECTORIES = [
    "10_orga",
    "20_literature",
    "30_data",
    "50_code",
    "70_results",
    "80_report",
    "90_presentation",
]


def create_project(project_name: str) -> None:
    """Create a project directory with standard subdirectories."""
    project_path = Path.cwd() / project_name

    if project_path.exists():
        print(f"Error: '{project_name}' already exists in the current directory.", file=sys.stderr)
        sys.exit(1)

    project_path.mkdir()
    print(f"Created project directory: {project_path}")

    for subdir in SUBDIRECTORIES:
        (project_path / subdir).mkdir()
        print(f"  + {subdir}/")

    print(f"\nProject '{project_name}' is ready.")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="make_project",
        description="Create a new project directory with standard subdirectories.",
    )
    parser.add_argument(
        "project_name",
        help="Name of the project to create",
    )

    args = parser.parse_args()
    create_project(args.project_name)


if __name__ == "__main__":
    main()
