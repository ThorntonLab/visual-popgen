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

# Mutation frequencies under selection (interactive Python)

This notebook requires Binder for the interactive features to function.
See {ref}`here <interactive_python_notebooks>` for more information.

This applet uses [moments](https://moments.readthedocs.io) {cite:p}`Jouganous2017-tg` to calculate the site-frequency spectrum in a sample of size 20 as a function of $\gamma = 2N_es$, the scaled strength of selection.

```{code-cell} python
import holoviews as hv
import moments

hv.extension('bokeh')

def fs_negative_selection(gamma):
    fs_neg = moments.Spectrum(
        moments.LinearSystem_1D.steady_state_1D(20, gamma=gamma)
    )[1:-1]
    b = hv.Histogram(([int(i)+1 for i in range(20)], fs_neg))
    b = b.redim(y=hv.Dimension('y',range=(0, 1.1*fs_neg.max())))
    b = b.opts(xlabel="Sample frequency", ylabel="Density")
    return b

kdims = [hv.Dimension('gamma',range=(-10, 10), step=1, default=0)]
fsplot = hv.DynamicMap(fs_negative_selection,
                       kdims=kdims).opts(framewise=True, width=500)
fsplot
```
