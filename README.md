# dna.sequence.analysis1
# Bioinformatics Practice Project: Using public gene expression data to compare biological conditions and create a reproducible scientific report.

# In order to be able to analyse dna sequences, it is crucial to first import matplotlib, which helps to make the graphs and to analyse the bioinformatics data. Pyplot is a function inside matplotlib which contains plotting function (and in this case we will shorten it to plt)

# Python also has a built-in collections module, which contains the tool Counter. Counter will be used to count the number of nucleotides and then, using pyplot, we will then plot the counts (discrete data) into a barplot (Remember the function in R: barplot(table(dat1$column)). Another package we will call is pathlib, and the tool imported will be Path, which allows us to read the files directly/create folders.

# It would be waste of time to copy the entire DNA sequence directly into VS, hence we use FASTA files, which we will extract from the NCBI genbank database. In this case, I'm going to use the genome of the West Nile Virus, a RNA virus which is mosquito-borne, originating in Uganda. 80% of patients will actually show no symptoms, however for vulnerable groups of people, like those over 50-65 years old or with weakened immune systems, it can be deadly. In recent years West Nile Virus has been found even in parts of Europe, including Italy, and in my small town of Varese, where there is an aging population. The west nile virus consists of multiple strains, for the sake of this project I will be using strain 956, as listed on NHI.




