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

# Python dependencies

The Python requirements for this book are:

```{code-cell}
---
tags: ['remove-input']
---

with open("../../../requirements.txt", "r") as f:
	x = f.readlines()
	print(''.join(x))
```

The above list is defined in `requirements.txt` in the `GitHub` repository.

The precise versions of all packages used to create this book are:

```{code-cell}
---
tags: ['remove-input']
---

import subprocess

lockfile = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE)
print(lockfile.stdout.decode('utf-8'))
```
