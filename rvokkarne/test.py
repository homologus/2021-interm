from Bio import SeqIO
from Bio.SeqUtils import GC

file = str(input('File: '))
reads = list(SeqIO.parse(file, 'fasta'))

seq1 = reads[0].seq.translate()

proteins = seq1.split('*')

