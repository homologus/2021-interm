from Bio import SeqIO
from Bio.SeqUtils import GC

file = str(input("File: "))
reads = list(SeqIO.parse(file, "fasta"))

if len(reads[0].seq)%3 == 1:
	reads[0].seq += 'NN'
elif len(reads[0].seq)%3 == 2:
	reads[0].seq += 'N'

rf1 = reads[0].seq
rf2 = reads[0].seq[1:len(reads[0].seq)-2]
rf3 = reads[0].seq[2:len(reads[0].seq)-1]
#rf4 = reads[0].seq.reverse_complement()
#rf5 = reads[0].seq[2:len(reads[0].seq)-1].reverse_complement()
#rf6 = reads[0].seq[1:len(reads[0].seq)-2].reverse_complement()

seqs1 = rf1.translate()
seqs2 = rf2.translate()
seqs3 = rf3.translate()
#seqs4 = rf4.translate()
#seqs5 = rf5.translate()
#seqs6 = rf6.translate()

lstart1 = []
lstart2 = []
lstart3 = []
#lstart4 = []
#lstart5 = []
#lstart6 = []
c1 = 0
c2 = 0
c3 = 0
#c4 = 0
#c5 = 0
#c6 = 0
n1 = 0
n2 = 0
n3 = 0
#n4 = 0
#n5 = 0
#n6 = 0

def locs(x, lstart, c):
	plength = 0
	startstop = {}
	for i in range(0, len(x)):
		if plength == 0:
			start = int(i)
		if x[i] != '*':
			plength += 1
		elif x[i] == '*':
			if plength > 100:
				lstart.append(start)
				startstop[lstart[c]] = int(i)
				c += 1
			plength = 0
	return startstop

def prot(x, lstart, n):
	sequences = {}
	proteins = x.split('*')
	for i in range(0, len(proteins)):
		if len(proteins[i]) > 100:
			sequences[lstart[n]] = ''.join(proteins[i])
			n += 1
	return sequences

locations1 = locs(seqs1, lstart1, c1)
proteins1 = prot(seqs1, lstart1, n1)

locations2 = locs(seqs2, lstart2, c2)
proteins2 = prot(seqs2, lstart2, n2)

locations3 = locs(seqs3, lstart3, c3)
proteins3 = prot(seqs3, lstart3, n3)

#locations4 = locs(seqs4, lstart4, c4)
#proteins4 = prot(seqs4, lstart4, n4)

#locations5 = locs(seqs5, lstart5, c5)
#proteins5 = prot(seqs5, lstart5, n5)

#locations6 = locs(seqs6, lstart6, c6)
#proteins6 = prot(seqs6, lstart6, n6)

print()
print('In reading frame 1:')
print(f'The proteins longer than 100 amino acids are: {proteins1}')
print(f'The endpoints of the proteins are: {locations1}')
print()
print('Reading frame 2 is adjusted by +1. In reading frame 2:')
print(f'The proteins longer than 100 amino acids are: {proteins2}')
print(f'The endpoints of the proteins are: {locations2}')
print()
print('Reading frame 3 is adjusted by +2. In reading frame 3:')
print(f'The proteins longer than 100 amino acids are: {proteins3}')
print(f'The endpoints of the proteins are: {locations3}')
print()
#print('Reading frame 4 is the reverse complement of reading frame 1. In reading frame 4:')
#print(f'The proteins longer than 100 amino acids are: {proteins4}')
#print(f'The endpoints of the proteins are: {locations4}')
#print()
#print('Reading frame 5 is the reverse complement of reading frame 1 adjusted by +1. In reading frame 5:')
#print(f'The proteins longer than 100 amino acids are: {proteins5}')
#print(f'The endpoints of the proteins are: {locations5}')
#print()
#print('Reading frame 6 is the reverse complement of reading frame 1 adjusted by +2. In reading frame 6:')
#print(f'The proteins longer than 100 amino acids are: {proteins6}')
#print(f'The endpoints of the proteins are: {locations6}')
#print()
