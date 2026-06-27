# make_project

A tiny CLI tool that scaffolds a standard project directory structure and sets up a GitHub repository — all with a single command.

## What it does

```
make_project my_amazing_project
```

1. Creates `my_amazing_project/` in your current directory with all standard subdirectories
2. Initialises `50_code/` as a git repository
3. Writes a default `README.md` inside `50_code/`
4. Creates a GitHub repo at `github.com/lukas-neumann-astro/my_amazing_project`
5. Commits and pushes the README to `main`

### Directory structure created

```
my_amazing_project/
├── 10_orga/
├── 20_literature/
├── 30_data/
├── 50_code/          ← git repo, linked to GitHub
│   └── README.md
├── 70_results/
├── 80_report/
└── 90_presentation/
```

## Prerequisites

**GitHub CLI** must be installed and authenticated:

```bash
brew install gh
gh auth login
```

## Installation

Install directly from GitHub (into your active virtual environment):

```bash
pip install git+https://github.com/lukas-neumann-astro/make_project.git
```

To install a specific tag or branch:

```bash
pip install git+https://github.com/lukas-neumann-astro/make_project.git@v0.1.0
```

## Usage

```bash
# Create project directories only
make_project <project_name>

# Create directories + initialise git + create a public GitHub repo
make_project <project_name> --github

# Create directories + initialise git + create a private GitHub repo
make_project <project_name> --private
```

`--private` implies `--github`, so you don't need to pass both.

## Development

Clone and install in editable mode:

```bash
git clone https://github.com/lukas-neumann-astro/make_project.git
cd make_project
pip install -e .
```

## License

MIT
