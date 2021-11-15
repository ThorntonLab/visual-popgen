# Population genetic data

Population genetics is about the genetic similarities/differences between individuals of a species.
Those individuals may be members of the same "population" or they may belong to different populations.
Now, with the ability to sequence DNA from preserved specimens, the two individuals in question need not exist in the same "generation".

This section deals, briefly, with what population genetic data "look like" and discusses various ways that we may summarize it.
We start from an empirical perspective.
One goes out into nature (or an experimental cage of fruit flies, or an experimental field location) and, through the application of some modern biotechnology, surveys *where* in the genome various individuals "out there" are identical at the DNA level and where they differ.

For the sake of clarity, we treat the biotechnology as a black box.
For our purposes, some magic happens that results in a collection of nucleotides that we understand to be the genome of an individual.
We also take for granted the computational steps needed to turn the magic into useful data.
All that we require right now is the following:

1. We know the order of the nucleotides in our data.
2. We know to which individual they belong.
3. We can assign a nucleotide to a particular parental chromosome.
   Take the case of sequencing a human.
   Humans are diploids, inheriting one copy of each autosome from each parent.
   For a given chromosome, we assume that we can distinguish data coming from the maternal and the paternal copy from one another.

From the above list, the third point is the strictest requirement.
In fact, such data are hard to obtain!
For now though, these complications do not matter.
At the end of this section you will find more discussion on the complications of real data.

In practice, we have other requirements on our data.
We will leave a discussion of those until later.

# Related readings

* {cite:t}`Kreitman1983-xr` provides a clear illustration of a variation table.
  It is also the first paper describing sequence-level variation at a gene.
* UK Biobank paper
* DGRP
* DPGP
* Arabidopsis 1k genomes
