# Installation

## Dependencies

### Required dependencies

- Python (3.11 or later)
- [numpy](https://www.numpy.org/) (2.0.0 or later)

## Stable release

Please install `hpc` in a Virtual environment so that its requirements don't tamper with your system's Python.

## conda

The easiest way to install `hpc` is using the `conda` package manager. `hpc` is available in the
[conda-forge](https://conda-forge.org/) channel. To install
you can use the following command:

```bash
conda install -c conda-forge hpc
```

If this works it will install `hpc` with all dependencies including Python, and you can skip the rest of the
installation instructions.

## Installing Python

For Python, we recommend using the Anaconda Distribution for Python 3, which is available
for download from https://www.anaconda.com/download/. The installer gives the option to
add `python` to your `PATH` environment variable. We will assume in the instructions
below that it is available in the path, such that `python`, `pip`, and `conda` are
all available from the command line.

Note that there is no hard requirement specifically for Anaconda's Python, but often it
makes installation of required dependencies easier using the conda package manager.

## From PyPI

To install the latest release of `hpc` from PyPI:

```bash
pip install hpc-utils
```

To install a specific version:

```bash
pip install hpc-utils==0.1.4
```

## From sources

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

Now you should be able to start this environment's Python with `python`, try
`import hpc` to see if the package is installed.

More details on how to work with conda environments can be found here:
https://conda.io/docs/user-guide/tasks/manage-environments.html

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
