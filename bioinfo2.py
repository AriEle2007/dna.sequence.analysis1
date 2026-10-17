#Are there differences in GC content across the genome?
from collections import Counter
import matplotlib.pyplot as plt
from pathlib import Path
# FASTA File
file_path = Path(__file__).with_name("GCA_000861085.1_ViralProj15431_genomic.fna")
with open(file_path, "r") as file:
    lines = file.readlines()

dna = "".join(
    line.strip()
    for line in lines
    if not line.startswith(">")
).upper()

#Step 1: splitting the DNA into regions of equal length
window_size = 200
step_size = 100 #arbitrary choice
positions = []
gc_values = []
#Use [] before loop when we do not yet know the values of the variables,
#since the loop will calculate them

for start in range(0, len(dna)-window_size, step_size):
    window = dna[start:start + window_size] #if only start, then it will just take eveyr 200th nucleotide
    counts = Counter(window)
    gc = (counts["G"] + counts["C"]) / len(window) * 100
    positions.append(start + window_size / 2)
    gc_values.append(gc) #Append = add one item to the end of the existing list
    #hence this allows us to get multiple values which we will use to plot


plt.plot(positions, gc_values)
plt.xlabel("Genome position (nucleotides)")
plt.ylabel("GC content (%)")
plt.title("GC Content Distribution across genome")
plt.show()



