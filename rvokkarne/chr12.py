from Bio import SeqIO
from Bio.SeqUtils import GC

file1 = str(input('chr12 file: '))
reads1 = list(SeqIO.parse(file1, 'fasta'))

file2 = str(input('Human ALDH2 DNA file: '))
reads2 = list(SeqIO.parse(file2, 'fasta'))

file3 = str(input('ALDH2 protein file: '))
reads3 = list(SeqIO.parse(file3, 'fasta'))

chr12 = ''.join(reads1[0].seq)

if chr12[111803961] == 'G':
	print('chr12 is normal.')
elif chr12[111803961] == 'A':
	print('chr12 is abnormal. Individual has alcohol flush.')

ALDH2 = reads2[0].seq
humanALDH2 = ALDH2.translate()
print(f"Individual's ALDH2 protein sequence: {humanALDH2}")

if humanALDH2 == ''.join(reads3[13].seq):
	print('The ALDH2 sequence matches.')
else:
	print('The ALDH2 sequence does not match.')
