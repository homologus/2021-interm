from Bio import SeqIO
from Bio.SeqUtils import GC

file = str(input("File: "))
reads = list(SeqIO.parse(file, 'fasta'))

#print(reads[0].seq.count())

count = len(reads[0].seq)
print(count)
