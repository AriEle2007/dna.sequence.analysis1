
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
# Calculate nucleotide counts
counts = Counter(dna)

# Calculate GC content
gc_content = (counts["G"] + counts["C"]) / len(dna) * 100

print("Sequence length:", len(dna))
print(f"GC content: {gc_content:.2f}%")

# Visualize nucleotide composition
bases = ["A", "T", "G", "C"]
values = [counts[base] for base in bases]

plt.bar(bases, values)
plt.xlabel("Nucleotide")
plt.ylabel("Frequency")
plt.title("DNA Nucleotide Composition")
plt.show()