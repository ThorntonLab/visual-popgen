(interactive_python_in_slides)=

# Using interactive Python applets in slideshow presentations

It is possible to use the interactive Python applications in slideshows.
Doing this makes this content available for lectures, etc..
You *do not* need internet access for the applets to function.

You need the following tools, all of which can be installed using `pip`:

* [jupyter](https://www.jupyter.org) notebook
* [RISE](https://rise.readthedocs.io/en/stable/)
* [hide_code](https://github.com/kirbs-/hide_code)

We highly recommend using a `virtualenv`

```{note}
The installation and setup instructions for `hide_code` did not "just work" for the author.
Each command needs a `--user` flag.

`RISE` is not compatible with `jupyter-lab`.
You must use the classic notebook interface.
```

Once the above are installed, you can generate slides, hide the code, and the slide will contain a working applet.

## Additional hints

* You may want to redefine the `height` and `width` output of the plots in order to better fill the slides.
  Doing so will cause the images to be far too big in the regular notebook view, but they will look good in the slide view.
* The pages of this book allow the Python code to be copied.
  If you mouse over a code block, a "page" icon appears in the top right.
  Click it, and the code block will be copied to your clip board.
  This copy method is the simplest way to get the examples into your own slideshows.

## Caveats and limitations

* Using this type of content in lecture slides basically commits you to bringing your own laptop to class.
  You need a fully-functional Python environment, etc., and you are unlikely to find such a thing on the ancient Windows PC at the podium in your classroom.
