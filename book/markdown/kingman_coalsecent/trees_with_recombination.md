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

(trees_with_recombination)=

# Trees with recombination

These figures recreate the concepts from Figure 5 of {cite:t}`Hudson1990-ff`.

The node label format is `id: birth time`.

```{code-cell}
---
"tags": ["remove-input"]
---

import msprime
from IPython.display import SVG
from myst_nb import glue

for replicate, ts in enumerate(
    msprime.sim_ancestry(
        10,
        ploidy=1,
        sequence_length=1e3,
        recombination_rate=5e-8,
        population_size=10000,
        random_seed=99112288,
        num_replicates=5,
    )
):
    node_labels={i: f"{i}: {int(ts.tables.nodes.time[i])}" for i in range(ts.num_nodes)}
    svg = ts.draw_svg(size=(800, 800), x_scale="treewise", y_axis=False, node_labels=node_labels)
    glue(f"rectree{replicate+1}", SVG(svg), display=False)
```

````{tabbed} Tree 1
```{glue:figure} rectree1
:figwidth: 800
:name: "rectree1"
```
````

````{tabbed} Tree 2
```{glue:figure} rectree2
:figwidth: 800
:name: "rectree2"
```
````

````{tabbed} Tree 3
```{glue:figure} rectree3
:figwidth: 800
:name: "rectree3"
```
````

````{tabbed} Tree 4
```{glue:figure} rectree4
:figwidth: 800
:name: "rectree4"
```
````

````{tabbed} Tree 5
```{glue:figure} rectree5
:figwidth: 800
:name: "rectree5"
```
````
