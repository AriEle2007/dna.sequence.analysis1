Overview

In bioinfo2.py, I analysed the distribution of GC content across the entire West Nile Virus genome strain 956. In order to be able to actually interpret the GC content variation, we need to know the genes, hence we need to use GenBank (see bioinfo3.py). Furthermore, we need to use Biobank, which is a library designed for working with biological sequences and annotated genome files. 

Results

Organism: West Nile virus,
Genome length: 10962,
CDS: polyprotein precursor, positions 97-10389

Hence the coding sequence occupies approximate 94% of the total genome, which is consistent with the compact genome organisation of the West Nile Virus. Now, in bioinfo3, I decided to seperate the regions based on this information seeing if the coding region contains a higher or lower GC content than the non-coding region(s).

5' UTR: 96 nt, GC = 43.75%,
Coding region: 10293 nt, GC = 51.02%,
3' UTR: 573 nt, GC = 52.88%,

These results indicate that 3' UTR Region contains the greatest GC content (52.88%), while 5'UTR contains the lowest GC content (43.75%). The coding region is 7.27% "richer" in GC-regions compared to the 5' UTR. GC-content alone does not contribute to the differences in the functional roles of the coding and non-coding regions, further requiring other evidence like secondary structure of RNA. Furthermore, the regions vary largely in size, with 5'UTR consisting of only 96 nucleotides, indicating that even one change in its nucleotides could drastically impact the % of GC regions, hence we need to be more cautious about drawing broad conclusions about the role of GC regions in coding vs non-coding RNA:
