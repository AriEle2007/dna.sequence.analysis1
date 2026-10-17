# dna.sequence.analysis1
# Bioinformatics Practice Project: Using public gene expression data to compare biological conditions and create a reproducible scientific report.

Overview

This project explores the nucleotide composition of the West Nile Virus genome, made available of NCBI.
The objective is to practice fundamental bioinformatics techniques, including sequence parsing, nucleotide frequency analysis, GC content calculation, and data visualization.

Dataset

Source: NCBI Genome Database
Assembly accession: GCA_000861085.1
File: GCA_000861085.1_ViralProj15431_genomic.fna
Organism: West Nile Virus, Strain 956

Research Questions

What is the nucleotide composition of the selected viral genome?
What percentage of the sequence consists of guanine (G) and cytosine (C)?
How are the four nucleotides distributed across the sequence?

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

Sequence length: 10962,
GC content: 51.06%,
See WestNileVirusNucleotideAnalysis.png for nucleotide distribution

Limitations

This preliminary analysis is descriptive. Nucleotide composition alone cannot establish evolutionary relationships, biological function, or disease-related properties. It is also based solely on the 956 strain, other strain analyses would need to be conducted.

Future Improvements

Compare nucleotide composition across different genomic regions.
Analyze additional published viral genomes.
Introduce Biopython for more advanced sequence analysis.

Data Source

NCBI Assembly: https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000861085.1/

