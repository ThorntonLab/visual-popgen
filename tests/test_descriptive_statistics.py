import math

import numpy as np
import pytest


@pytest.mark.parametrize("seed", [10234, 91246412])
def test_heterozygosity_homozygosity(seed):
    rng = np.random.Generator(np.random.MT19937(seed=seed))

    for _ in range(10):
        data = rng.integers(1, high=10, size=6)
        nsam = data.sum()
        heterozygosity = 0.0
        homozygosity = 0.0
        for d in data:
            heterozygosity += d * (nsam - d)
            homozygosity += d * (d - 1)
        heterozygosity /= nsam * (nsam - 1)
        homozygosity /= nsam * (nsam - 1)
        assert math.isclose(
            heterozygosity, 1.0 - homozygosity
        ), f"{heterozygosity} {1.0 - homozygosity}"
