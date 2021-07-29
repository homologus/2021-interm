from Bio import SeqIO
from Bio.SeqUtils import GC

file = str(input('File: '))
reads = list(SeqIO.parse(file, 'fasta'))

normal = reads[0].seq.translate()
flush = reads[1].seq.translate()

for i in range(0, len(normal)):
	for j in range(0, len(flush)):
		if i != j:
			continue
		if normal[i] != flush[j]:
			print(f'The normal and flush proteins differ at {i}.')
			print(f'Normal amino acid: {normal[i]}')
			print(f'Flush amino acid: {flush[j]}')
