from Bio import SeqIO
from Bio.SeqUtils import GC

for i in SeqIO.parse("small-genome", "fasta"):
	print(len(i))
	print(GC(i.seq))
