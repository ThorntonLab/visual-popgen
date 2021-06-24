---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(descriptive_statistics)=

```{code-cell} python
---
tags: [hide-input]
---
import math

from myst_nb import glue
import msprime
import numpy as np

ts = msprime.sim_ancestry(5, population_size=1.0, recombination_rate=0.,
                          random_seed=54321, sequence_length=1.0,
                          discrete_genome=False)
ts = msprime.sim_mutations(ts, rate=0.25, random_seed=12345,
                           model=msprime.JC69(), discrete_genome=False)
```

# Simple descriptive statistics

```{code-cell} python
---
tags: [hide-input]
---
alleles = ('A','C','G','T')
gmatrix = ts.genotype_matrix(alleles=alleles).T
haplotypes = np.zeros(len(gmatrix.flatten()), dtype=np.unicode_)
for i, a in enumerate(gmatrix.flatten()):
    haplotypes[i] = alleles[a]
haplotypes = haplotypes.reshape(gmatrix.shape)
print(haplotypes)
```

```{code-cell} python
---
tags: [hide-input]
---
print(gmatrix)
```

## The number of variable sites

## The number of pairwise differences

```{code-cell} python
---
tags: [hide-input]
---
ndiffs = 0
for i in range(gmatrix.shape[0]):
    for j in range(i + 1, gmatrix.shape[0]):
        for k,l in zip(gmatrix[i,:], gmatrix[j,:]):
            if k != l:
                ndiffs += 1
ncomps = gmatrix.shape[0] * (gmatrix.shape[0] - 1) / 2
ndiffs = ndiffs / ncomps
assert math.isclose(ndiffs, ts.diversity([[i for i in ts.samples()]])[0])
glue("mean_diffs", np.round(ndiffs, 4), display=False)
```

The answer here is {glue:text}`mean_diffs`.

## Heterozygosity

## Homozygosity

## Normalizing by the length of a genomic region

## Ancestral/derived and minor/major alleles

# The site (or allele) frequency spectrum

# Correlations amongst variable sites ("linkage disequilibrium")
