from Bio import SeqIO
from Bio.SeqUtils import GC

file = str(input('File: '))
reads = list(SeqIO.parse(file, 'fasta'))

normal = reads[0].seq.translate()
flush = reads[1].seq.translate()


