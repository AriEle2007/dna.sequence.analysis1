# dna.sequence.analysis1
# Bioinformatics Practice Project: West Nile Virus
Overview

This project explores the nucleotide composition of the West Nile Virus genome, made available of NCBI.
The objective is to practice fundamental bioinformatics techniques, including sequence parsing, nucleotide frequency analysis, GC content calculation, and data visualization.

In bioinfo2.py, I analysed the distribution of GC content across the entire West Nile Virus genome strain 956. In order to be able to actually interpret the GC content variation, we need to know the genes, hence we need to use GenBank (see bioinfo3.py). Furthermore, we need to use Biobank, which is a library designed for working with biological sequences and annotated genome files. 

Dataset

Source: NCBI Genome Database
Assembly accession: GCA_000861085.1
File: GCA_000861085.1_ViralProj15431_genomic.fna
Organism: West Nile Virus, Strain 956

Note: I used the GenBank file which is the raw data, user-submitted, and non-curated. It can contain high redundancy; including multiple overlapping or duplicate submissions for the same locus and/or hundreds of thousands of diverse, rare, or uncultured species.

Research Questions

Part A

What is the nucleotide composition of the selected viral genome?
What percentage of the sequence consists of guanine (G) and cytosine (C)?
How are the four nucleotides distributed across the sequence?

Part B

What is the length of the coding sequence?

Part C

How does GC content vary between the coding region and non-coding regions?

Methods

The analysis was conducted using Python.
collections.Counter to calculate nucleotide frequencies.
matplotlib to visualize nucleotide composition.
Basic sequence processing to read FASTA-formatted genomic data.

Notes Method

In order to be able to analyse dna sequences, it is crucial to first import matplotlib, which helps to make the graphs and to analyse the bioinformatics data. Pyplot is a function inside matplotlib which contains plotting function (and in this case we will shorten it to plt)
Python also has a built-in collections module, which contains the tool Counter. Counter will be used to count the number of nucleotides and then, using pyplot, we will then plot the counts (discrete data) into a barplot (Remember the function in R: barplot(table(dat1$column)). Another package we will call is pathlib, and the tool imported will be Path, which allows us to read the files directly/create folders.
It would be waste of time to copy the entire DNA sequence directly into VS, hence we use FASTA files, which we will extract from the NCBI genbank database. 


West Nile Virus Short Description

In this case, I'm going to use the genome of the West Nile Virus, a RNA virus which is mosquito-borne, originating in Uganda. 80% of patients will actually show no symptoms, however for vulnerable groups of people, like those over 50-65 years old or with weakened immune systems, it can be deadly. In recent years West Nile Virus has been found even in parts of Europe, including Italy, and in my small town of Varese, where there is an aging population. The West Nile Virus consists of multiple strains, for the sake of this project I will be using strain 956, as listed on NIH.


Results

Part A: A, C, T, G Distribution

Sequence length: 10962,
GC content: 51.06%,
See WestNileVirusNucleotideAnalysis.png for nucleotide distribution

Part B: Coding Sequence vs Non-coding Sequence

Organism: West Nile virus,
Genome length: 10962,
CDS: polyprotein precursor, positions 97-10389

Hence the coding sequence occupies approximate 94% of the total genome, which is consistent with the compact genome organisation of the West Nile Virus. 

Part C: GC content variation between coding and non-coding regions.

Now, in bioinfo3, I decided to seperate the regions based on this information seeing if the coding region contains a higher or lower GC content than the non-coding region(s).

5' UTR: 96 nt, GC = 43.75%,
Coding region: 10293 nt, GC = 51.02%,
3' UTR: 573 nt, GC = 52.88%,

These results indicate that 3' UTR Region contains the greatest GC content (52.88%), while 5'UTR contains the lowest GC content (43.75%). The coding region is 7.27% "richer" in GC-regions compared to the 5' UTR. GC-content alone does not contribute to the differences in the functional roles of the coding and non-coding regions, further requiring other evidence like secondary structure of RNA. Furthermore, the regions vary largely in size, with 5'UTR consisting of only 96 nucleotides, indicating that even one change in its nucleotides could drastically impact the % of GC regions, hence we need to be more cautious about drawing broad conclusions about the role of GC regions in coding vs non-coding RNA:

Limitations

This preliminary analysis is descriptive. Nucleotide composition alone cannot establish evolutionary relationships, biological function, or disease-related properties. It is also based solely on the 956 strain, other strain analyses would need to be conducted.

Future Improvements

Compare nucleotide composition across different genomic regions.
Analyze additional published viral genomes.
Introduce Biopython for more advanced sequence analysis.

Data Source

NCBI Assembly: https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000861085.1/
