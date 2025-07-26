# Installation

## Dependencies

### Required dependencies

- Python (3.11 or later)
- [numpy](https://www.numpy.org/) (2.0.0 or later)

### Optional dependencies

#### Development dependencies
- nbval (0.11.0 or later)
- pre-commit (3.7.1 or later)
- pre-commit-hooks (4.6.0 or later)
- pytest (8.2.2 or later)
- pytest-cov (5.0.0 or later)
- coverage

#### Documentation dependencies
- mkdocs (1.5.3 or later)
- mkdocs-material (9.5.3 or later)
- mkdocstrings (0.24.0 or later)
- mkdocstrings-python (1.7.5 or later)
- mike (2.1.3 or later)
- mkdocs-jupyter (0.25.1 or later)
- mkdocs-autorefs (1.2 or later)
- mkdocs-macros-plugin (1.3.7 or later)
- mkdocs-table-reader-plugin (3.1.0 or later)
- mkdocs-mermaid2-plugin (1.2.1 or later)
- jupyter-contrib-nbextensions (0.7.0 or later)
- notebook (< 7.0)
- jupyter

## Installation Methods

Please install `hpc` in a virtual environment so that its requirements don't tamper with your system's Python.

### Using Pixi (Recommended)

[Pixi](https://prefix.dev/docs/pixi/overview) is a package manager and environment manager developed by Prefix.dev. It's designed to create reproducible environments and is used in this project for dependency management.

#### Installing Pixi

If you don't have Pixi installed, you can install it following the instructions on the [Pixi installation page](https://prefix.dev/docs/pixi/installation).

For Windows:
```powershell
# Using PowerShell
iwr -useb https://pixi.sh/install.ps1 | iex
```

For Linux/macOS:
```bash
# Using curl
curl -fsSL https://pixi.sh/install.sh | bash
```

#### Setting up the environment with Pixi

1. Clone the repository:
```bash
git clone https://github.com/Serapieum-of-alex/hpc.git
cd hpc
```

2. Install dependencies using Pixi:
```bash
pixi install
```

This will create a reproducible environment with all the required dependencies based on the pixi.lock file.

#### Using different environments

The project defines three environments in the pyproject.toml file:

1. **default**: Basic environment with minimal dependencies
```bash
# Activate the default environment
pixi shell
```

2. **dev**: Development environment with testing tools
```bash
# Run a command in the dev environment
pixi run --environment dev pytest
```

3. **docs**: Documentation environment with tools for building docs
```bash
# Run a command in the docs environment
pixi run --environment docs mkdocs build
```

### Using Conda

The easiest way to install `hpc` is using the `conda` package manager. `hpc` is available in the
[conda-forge](https://conda-forge.org/) channel. To install
you can use the following command:

```bash
conda install -c conda-forge hpc
```

If this works it will install `hpc` with all dependencies including Python, and you can skip the rest of the
installation instructions.

### Using Pip (PyPI)

To install the latest release of `hpc` from PyPI:

```bash
pip install hpc-utils
```

To install a specific version:

```bash
pip install hpc-utils==0.1.4
```

### Installing Python

For Python, we recommend using the Anaconda Distribution for Python 3, which is available
for download from https://www.anaconda.com/download/. The installer gives the option to
add `python` to your `PATH` environment variable. We will assume in the instructions
below that it is available in the path, such that `python`, `pip`, and `conda` are
all available from the command line.

Note that there is no hard requirement specifically for Anaconda's Python, but often it
makes installation of required dependencies easier using the conda package manager.

### From sources

The sources for `hpc` can be downloaded from the [Github repo](https://github.com/Serapieum-of-alex/hpc).

You can either clone the public repository:

```bash
git clone git://github.com/Serapieum-of-alex/hpc
```

Or download the [tarball](https://github.com/Serapieum-of-alex/hpc/tarball/master):

```bash
curl -OJL https://github.com/Serapieum-of-alex/hpc/tarball/main
```

Once you have a copy of the source, you can install it with:

```bash
python -m pip install .
```

To install directly from GitHub (from the HEAD of the main branch):

```bash
pip install git+https://github.com/Serapieum-of-alex/hpc.git
```

or from Github from a specific release:

```bash
pip install git+https://github.com/Serapieum-of-alex/hpc.git@{release}
```

If you are planning to make changes and contribute to the development of `hpc`, it is
best to make a git clone of the repository, and do an editable install in the location
of your clone. This will not move a copy to your Python installation directory, but
instead create a link in your Python installation pointing to the folder you installed
it from, such that any changes you make there are directly reflected in your install.

```bash
git clone https://github.com/Serapieum-of-alex/hpc.git
cd hpc
pip install -e .
```

## Check if the installation is successful

To check if the install is successful, try importing the package:

```python
import hpc
print(hpc.__version__)
```

This should run without errors and display the version number.

!!! note
    This documentation was generated on 2025-07-24

    Documentation for the development version:
    https://hpc.readthedocs.org/en/latest/

    Documentation for the stable version:
    https://hpc.readthedocs.org/en/stable/
