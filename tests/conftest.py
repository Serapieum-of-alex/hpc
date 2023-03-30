import numpy as np
import pytest

@pytest.fixture(scope="module")
def arr() -> np.ndarray:
    return np.load("tests/data/arr.npy")