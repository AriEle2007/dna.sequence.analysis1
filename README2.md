Overview

In bioinfo2.py, I analysed the distribution of GC content across the entire West Nile Virus genome strain 956. In order to be able to actually interpret the GC content variation, we need to know the genes, hence we need to use GenBank (see bioinfo3.py). Furthermore, we need to use Biobank, which is a library designed for working with biological sequences and annotated genome files. 

Results

Organism: West Nile virus,
Genome length: 10962,
CDS: polyprotein precursor, positions 97-10389

Hence the coding sequence occupies approximate 94% of the total genome. Now, in bioinfo3, I decided to seperate the regions based on this information seeing if the coding region contains a higher or lower GC content than the non-coding region(s).
