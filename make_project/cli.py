"""Command-line interface for make_project."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

GITHUB_ORG = "lukas-neumann-astro"

SUBDIRECTORIES = [
    "10_orga",
    "20_literature",
    "30_data",
    "50_code",
    "70_results",
    "80_report",
    "90_presentation",
]

README_TEMPLATE = """\
# {project_name}

## Overview

_Short description of the project._

## Structure

| Folder | Purpose |
|--------|---------|
| `10_orga/` | Organisation, notes, meeting minutes |
| `20_literature/` | Papers and references |
| `30_data/` | Raw and processed data |
| `50_code/` | Source code (this repo) |
| `70_results/` | Output figures and tables |
| `80_report/` | Report drafts |
| `90_presentation/` | Presentation files |

## Getting started

```bash
git clone https://github.com/lukas-neumann-astro/{project_name}.git
```
"""


def check_gh_cli() -> None:
    """Ensure the GitHub CLI is installed and authenticated."""
    if shutil.which("gh") is None:
        print(
            "Error: GitHub CLI ('gh') is not installed.\n"
            "Install it with:  brew install gh\n"
            "Then authenticate:  gh auth login",
            file=sys.stderr,
        )
        sys.exit(1)

    result = subprocess.run(
        ["gh", "auth", "status"], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(
            "Error: GitHub CLI is not authenticated.\n"
            "Run:  gh auth login",
            file=sys.stderr,
        )
        sys.exit(1)


def init_code_repo(code_path: Path, project_name: str, visibility: str = "public") -> None:
    """Initialise a git repo in 50_code, create README, and push to GitHub."""

    # Write README.md
    readme = code_path / "README.md"
    readme.write_text(
        README_TEMPLATE.format(project_name=project_name, org=GITHUB_ORG)
    )
    print("    Wrote README.md")

    # git init
    subprocess.run(["git", "init"], cwd=code_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "branch", "-M", "main"], cwd=code_path, check=True, capture_output=True
    )
    print("    Initialised git repository (branch: main)")

    # Stage and commit README so --push has something to push
    subprocess.run(["git", "add", "README.md"], cwd=code_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "Initial commit"],
        cwd=code_path, check=True, capture_output=True,
    )
    print("    Created initial commit")

    # Create GitHub repo under the org and push
    subprocess.run(
        [
            "gh", "repo", "create",
            f"{GITHUB_ORG}/{project_name}",
            f"--{visibility}",
            "--source", str(code_path),
            "--remote", "origin",
            "--push",
            "--description", f"Code repository for project: {project_name}",
        ],
        check=True,
    )
    print(f"    Created GitHub repo and pushed: https://github.com/lukas-neumann-astro/{project_name}")


def create_project(
    project_name: str,
    use_github: bool = False,
    visibility: str = "public",
) -> None:
    """Create a project directory with standard subdirectories."""
    project_path = Path.cwd() / project_name

    if project_path.exists():
        print(
            f"Error: '{project_name}' already exists in the current directory.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Check gh CLI before creating any directories
    if use_github:
        check_gh_cli()

    # Create directories
    project_path.mkdir()
    print(f"Created project directory: {project_path}")

    code_path = None
    for subdir in SUBDIRECTORIES:
        subdir_path = project_path / subdir
        subdir_path.mkdir()
        print(f"  + {subdir}/")
        if subdir == "50_code":
            code_path = subdir_path

    # Optionally initialise git + GitHub repo inside 50_code
    if use_github:
        print("\n  Initialising code repository ...")
        init_code_repo(code_path, project_name, visibility=visibility)

    print(f"\nProject '{project_name}' is ready.")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="make_project",
        description=(
            "Create a new project directory with standard subdirectories.\n"
            "Optionally initialise 50_code/ as a git repo and push it to GitHub."
        ),
    )
    parser.add_argument(
        "project_name",
        help="Name of the project (also used as the GitHub repository name)",
    )
    parser.add_argument(
        "--github",
        action="store_true",
        default=False,
        help="Initialise 50_code/ as a git repo and create a public GitHub repository",
    )
    parser.add_argument(
        "--private",
        action="store_true",
        default=False,
        help="Make the GitHub repository private (implies --github)",
    )

    args = parser.parse_args()

    # --private implies --github
    use_github = args.github or args.private
    visibility = "private" if args.private else "public"

    create_project(args.project_name, use_github=use_github, visibility=visibility)


if __name__ == "__main__":
    main()
