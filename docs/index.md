# HPC - Numpy Utility Package

[![Python Versions](https://img.shields.io/pypi/pyversions/hpc.png)](https://img.shields.io/pypi/pyversions/hpc)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Documentation Status](https://readthedocs.org/projects/hpc/badge/?version=latest)](https://hpc.readthedocs.io/en/latest/?badge=latest)

## Overview

**HPC** is a numpy utility package focused on high-performance computing applications. It provides efficient functions for indexing and manipulating numpy arrays without using loops, resulting in faster execution times.

## Main Features

- Fast indexing of numpy arrays without using loops
- Efficient pixel extraction from arrays with optional masking
- Location of values in grids with coordinate mapping

## Quick Start

```python
import numpy as np
import hpc

# Create a sample array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get indices of all non-zero values
i, j = hpc.get_indices(arr, None)
print(f"Row indices: {i}")
print(f"Column indices: {j}")

# Get indices of specific value
i, j = hpc.get_indices(arr, 5)
print(f"Row indices for value 5: {i}")
print(f"Column indices for value 5: {j}")

# Get pixels with masking
mask = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
pixels = hpc.get_pixels(arr, mask)
print(f"Masked pixels: {pixels}")
```

## Installation

For installation instructions, see the [Installation](installation.md) page.

## API Documentation

For detailed API documentation, see the [API Documentation](api/indexing.md) section.

!!! note
    This documentation was generated on 2025-07-24.
