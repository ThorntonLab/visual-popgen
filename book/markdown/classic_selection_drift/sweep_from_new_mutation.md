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

# Selective "sweeps" (from new mutations)

This image recreates results from Figure 3 of {cite:t}`Kim2002-to`.

```{code-cell}
---
"tags": [ "remove-input" ]
---

import holoviews as hv
import msprime
import numpy as np
import pandas as pd

hv.extension("bokeh")

Ne = 5e5
L = 4e5
n = 5
s = 1e-3
r = 1e-8
THETA = 0.005

wins = np.linspace(0, L, 400)
mids = (wins[1:] + wins[:-1]) / 2
RHO = [800.0]
TAU = [0.0, 0.1]
tauvals = []
midpoints = []
diversityvals = []
thetavals = []
faywuvals = []
replicatevals = []

ett = 0.0
for i in range(1, n):
    ett += 1.0 / i

assert ett > 0.0


def divcheck(x):
    return [0.0]


def FayWu(x):
    if x[0] == 0 or x[0] == 2 * n:
        return 0
    return [x[0] ** 2]


for rho in RHO:
    for tau in TAU:
        sweep_model = msprime.SweepGenicSelection(
            position=L / 2,  # middle of chrom
            start_frequency=1.0 / (2 * Ne),
            end_frequency=1.0 - (1.0 / (2 * Ne)),
            s=s,
            dt=1e-6,
        )
        for replicate, ts in enumerate(
            msprime.sim_ancestry(
                n,
                model=[
                    msprime.StandardCoalescent(duration=tau * 2 * Ne),
                    sweep_model,
                    msprime.StandardCoalescent(),
                ],
                population_size=Ne,
                recombination_rate=rho / (L * 4 * Ne),
                sequence_length=L,
                num_replicates=10,
                random_seed=12345,
            )
        ):
            ts = msprime.sim_mutations(
                ts, rate=THETA / (4 * Ne), discrete_genome=False, random_seed=54321
            )
            diversity = ts.diversity(windows=wins, mode="site")
            segsites = ts.segregating_sites(windows=wins, mode="site")
            H = (
                2
                * ts.sample_count_stat(
                    [[i for i in ts.samples()]],
                    f=FayWu,
                    output_dim=1,
                    mode="site",
                    windows=wins,
                    polarised=True,
                )
                / (2 * n * (2 * n - 1))
            )

            for i, j, k, l in zip(wins, diversity, segsites, H):
                tauvals.append(tau)
                midpoints.append(i)
                diversityvals.append(j)
                thetavals.append(k / ett)
                faywuvals.append(l[0])
                replicatevals.append(replicate)

pddata = pd.DataFrame(
    {
        "tau": tauvals,
        "midpoint": midpoints,
        "diversity": diversityvals,
        "theta": thetavals,
        "thetah": faywuvals,
        "replicate": replicatevals,
    }
)

key_dimensions = [
    ("midpoint", "Window midpoint"),
    ("tau", "Fixation time (in past)"),
    ("replicate", "Replicate number"),
]
value_dimensions = [
    ("diversity", "Diversity"),
    ("theta", "Theta"),
    ("thetah", "ThetaH"),
]
hv_data = hv.Table(pddata, key_dimensions, value_dimensions)

ymin = 0.0
ymax = 1.1 * max(
    pddata["diversity"].max(), pddata["theta"].max(), pddata["thetah"].max()
)

div_curves = hv_data.to.curve("Window midpoint", "Diversity", label="Tajima/Nei")
S_curves = hv_data.to.curve("Window midpoint", "Theta", label="Watterson")
H_curves = hv_data.to.curve("Window midpoint", "ThetaH", label="Fay/Wu")
neutral = hv.HLine(THETA, label="Neutral expectation")
annotations = hv.Arrow(L // 2, 0.65 * ymax, "Location of sweep", "v")
(div_curves * S_curves * H_curves * neutral * annotations).opts(
    hv.opts.Curve(color=hv.Cycle("Colorblind"), ylim=(ymin, ymax)),
    hv.opts.HLine(color="grey", alpha=0.5),
    hv.opts.Text(text_font_size="13px"),
    hv.opts.Overlay(height=500, show_frame=False, width=700),
)
```
