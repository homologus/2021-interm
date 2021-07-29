from Bio import SeqIO
from Bio.SeqUtils import GC

file = str(input('File: '))
reads = list(SeqIO.parse(file, 'fasta'))

for i in range(len(reads)):
	for j in range(len(reads)):
		if i+j+1 >= len(reads):
			break
		seq1 = reads[i].seq
		seq2 = reads[i+j+1].seq
		n = 0
		for k in range(len(seq1)):
			if seq1[k] != seq2[k]:
				n += 1
		if n > 1:
			print(f'{reads[i].id} and {reads[i+j+1].id}: {n} differences')
		elif n == 1:
			print(f'{reads[i].id} and {reads[i+j+1].id}: {n} difference')
