#Interpretation GC Content
from Bio import SeqIO #Seq10 loads the annotated genome record
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

# Locate the annotated genome file
file_path = Path(__file__).with_name("genomic.gbff")

# Read the GenBank record
record = SeqIO.read(file_path, "genbank")

print("Organism:", record.annotations.get("organism"))
print("Genome length:", len(record.seq))

# Extract annotated genes and coding regions
for feature in record.features:

    if feature.type in ["gene", "CDS"]:
        #CDS = coding sequence

        start = int(feature.location.start) + 1
        end = int(feature.location.end)

        name = feature.qualifiers.get(
            "gene",
            feature.qualifiers.get("product", ["Unknown"])
        )[0]

        print(
            f"{feature.type}: {name}, "
            f"positions {start}-{end}"
        )

#Find the CDS
cds = next(
    feature for feature in record.features
    if feature.type == "CDS"
)

start = int(cds.location.start)
end = int(cds.location.end)
#Note: location will give the nucleotides

# Extract each genomic region
utr_5 = str(record.seq[:start])
coding = str(record.seq[start:end])
utr_3 = str(record.seq[end:])

# Calculate GC content of a sequence
def calculate_gc(sequence):
    counts = Counter(sequence)
    valid = sum(counts[base] for base in "ATGC")
    if valid == 0:
        return 0
    return (counts["G"] + counts["C"]) / valid * 100

regions = {
    "5' UTR": utr_5,
    "Coding region": coding,
    "3' UTR": utr_3
}

gc_values = []

for name, sequence in regions.items():
    gc = calculate_gc(sequence)
    gc_values.append(gc)

    print(f"{name}: {len(sequence)} nt, GC = {gc:.2f}%")

# Plot comparison
plt.figure(figsize=(8, 5))
plt.bar(regions.keys(), gc_values)
plt.ylabel("GC content (%)")
plt.title("GC Content Across West Nile Virus Genome Regions")
plt.show()
