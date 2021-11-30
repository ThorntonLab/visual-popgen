(observable_in_slides)=

# Using Observable content in Jupyter presentations

You can display the observable content in Jupyter notebooks (and slideshows).
Note that you *do need* internet access for the content to display!

The following Python code will display {ref}`this <fixation_in_diploid_population>` Observable widget in a Jupyter output cell:

``` python
from IPython.core.display import display, HTML
script="""
<iframe width="75%" height="750" frameborder="0"
  src="https://observablehq.com/embed/@molpopgen/fixation-under-directional-selection?cells=detail_plot%2Cviewof+N%2Cviewof+num_copies%2Cviewof+selection_coefficient%2Cviewof+dominance%2Cviewof+show_genotypes"></iframe>
"""
display(HTML(script))
```

Using the tools described {ref}`here <interactive_python_in_slides>`, you can hide the Python code needed to display the applet.

## Additional hints

* The `iframe` code needed to embed the Observable content can be copied from the source code for this project.
  Alternately, you can generate your own embed code manually from the [author's collection](https://www.observablehq.com/@molpopgen).

## Limitations

* The applications may be quite small in the slides.
  We are currently not sure if there is a way to rescale them.
