from Bio import SeqIO
from Bio.SeqUtils import GC

inp=str(input("Input file name:"))
reads = list(SeqIO.parse(inp, "fasta"))
seq = list(SeqIO.read(inp, "fasta"))

total_length = 0

for i in range(0, len(reads)):
    temp=len(reads[i].seq)
    total_length=total_length+temp


print(f"Total length is: {total_length}")
print(f"GC Content is: {GC(seq)}")
