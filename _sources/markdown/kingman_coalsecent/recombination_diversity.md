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

# Variation in diversity along a recombining genome (interactive)

This notebook is interactive.
See {ref}`here <interactive_notebooks>` for more information.

This applet is another take on the concepts shown in Figure 5 of {cite:t}`Hudson1990-ff`.

```{code-cell} python
---
tags: ['hide-input']
---

import msprime
import numpy as np
import panel as pn
import holoviews as hv

hv.extension('bokeh', 'matplotlib')

def branch_diversity_along_tree(rho, n, sequence_length=1e6, num_windows=500):
    wins = np.linspace(0, sequence_length, num_windows)
    mids = (wins[1:] - wins[:1])/2
    ts = msprime.sim_ancestry(n, ploidy=1,
                              sequence_length=sequence_length,
                              recombination_rate=rho/4/sequence_length)
    assert ts.num_samples == n
    diversity = ts.diversity(windows=wins, mode="branch").flatten()
    return hv.Curve((mids, diversity)).opts(tools=["box_select"]).redim(y=hv.Dimension('y',
                                                                                       range=(0, 1.1*diversity.max()))).opts(xlabel="Window midpoint", ylabel="Diversity (branch stat)")

divplot = hv.DynamicMap(branch_diversity_along_tree,
                        kdims=['rho', 'n']).redim.range(rho=(0, 1000), n=(10, 100)).opts(framewise=True, width=500)
divplot
```