# make_project

A tiny CLI tool that scaffolds a standard project directory structure with a single command.

## Directory structure created

```
<project_name>/
├── 10_orga/
├── 20_literature/
├── 30_data/
├── 50_code/
├── 70_results/
├── 80_report/
└── 90_presentation/
```

## Installation

Install directly from GitHub (into your active virtual environment):

```bash
pip install git+https://github.com/<your-username>/make_project.git
```

To install a specific tag or branch:

```bash
pip install git+https://github.com/<your-username>/make_project.git@v0.1.0
pip install git+https://github.com/<your-username>/make_project.git@main
```

## Usage

```bash
make_project <project_name>
```

Example:

```bash
make_project my_research_2025
```

Output:

```
Created project directory: /Users/you/current_dir/my_research_2025
  + 10_orga/
  + 20_literature/
  + 30_data/
  + 50_code/
  + 70_results/
  + 80_report/
  + 90_presentation/

Project 'my_research_2025' is ready.
```

The project folder is always created **inside your current working directory**.

## Development

Clone and install in editable mode:

```bash
git clone https://github.com/<your-username>/make_project.git
cd make_project
pip install -e .
```

## License

MIT
