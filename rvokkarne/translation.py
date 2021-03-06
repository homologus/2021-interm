import sys, re

# read full SARS-CoV2 genome and save it to a list
file = str(input("File: "))
f = open(file, 'r')
lines = f.readlines()

title_re = re.compile('>(\S+)')
notitle_re = re.compile('^(\S+)')

DNAseq = list()

for line in lines:
	outh = title_re.search(line)
	if outh:
		continue
	else:
		outl = notitle_re.search(line)
		outm = outl.group(1)
		temp = list(outm)
		DNAseq += temp

# dictionary of amino acids + empty lists for later use
amino_acids = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}

protein1 = list()
protein2 = list()
protein3 = list()
proteinlength1 = 0
proteinlength2 = 0
proteinlength3 = 0
start1 = 0
start2 = 0
start3 = 0
proteinstart1 = list()
proteinstart2 = list()
proteinstart3 = list()
aastart1 = list()
aastart2 = list()
aastart3 = list()
proteinstop1 = list()
proteinstop2 = list()
proteinstop3 = list()
idx1 = list()
idx2 = list()
idx3 = list()
list1 = list()
list2 = list()
list3 = list()
seq1 = list()
seq2 = list()
seq3 = list()
startstop1 = list()
startstop2 = list()
startstop3 = list()

# reading frame 1
for i in range(0, len(DNAseq) - 2, 3):
	tempcodon1 = list()
	tempcodon1 += DNAseq[i:i+3]
	if len(tempcodon1) < 3:
		break
	codon1 = ''.join(tempcodon1)
	p1 = amino_acids[codon1]
	if proteinlength1 == 0:
		start1 = int(i/3)
		proteinstart1.append(start1)
	if p1 != '*':
		proteinlength1 += 1
	elif p1 == '*':
		if proteinlength1 > 100:
			aastart1.append(start1)
			idx1.append(len(proteinstop1))
		proteinstop1.append(int(i/3))
		proteinlength1 = 0
	protein1.append(p1)

proteinstop1.append(len(protein1) - 1)

for i in range(0, len(idx1)):
	x = idx1[i]
	a = proteinstart1[x]
	b = proteinstop1[x] + 1
	list1.append(protein1[a:b])
	str1 = ''.join(list1[i])
	seq1.append(str1)

sequences1 = {aastart1[i]: seq1[i] for i in range(len(aastart1))}
for i in idx1:
	startstop1.append([(proteinstart1[i], proteinstop1[i]), proteinstop1[i] - proteinstart1[i] + 1])

# reading frame 2
for i in range(0, len(DNAseq) - 2, 3):
	tempcodon2 = list()
	tempcodon2 += DNAseq[i+1:i+4]
	if len(tempcodon2) < 3:
		break
	codon2 = ''.join(tempcodon2)
	p2 = amino_acids[codon2]
	if proteinlength2 == 0:
		start2 = int(i/3)
		proteinstart2.append(start2)
	if p2 != '*':
		proteinlength2 += 1
	elif p2 == '*':
		if proteinlength2 > 100:
			aastart2.append(start2)
			idx2.append(len(proteinstop2))
		proteinstop2.append(int(i/3))
		proteinlength2 = 0
	protein2.append(p2)

proteinstop2.append(len(protein2) - 1)

for i in range(0, len(idx2)):
	x = idx2[i]
	a = proteinstart2[x]
	b = proteinstop2[x] + 1
	list2.append(protein2[a:b])
	str2 = ''.join(list2[i])
	seq2.append(str2)

sequences2 = {aastart2[i]: seq2[i] for i in range(len(aastart2))}
for i in idx2:
	startstop2.append([(proteinstart2[i], proteinstop2[i]), proteinstop2[i] - proteinstart2[i] + 1])

# reading frame 3
for i in range(0, len(DNAseq) - 2, 3):
	tempcodon3 = list()
	tempcodon3 += DNAseq[i+2:i+5]
	if len(tempcodon3) < 3:
		break
	codon3 = ''.join(tempcodon3)
	p3 = amino_acids[codon3]
	if proteinlength3 == 0:
		start3 = int(i/3)
		proteinstart3.append(start3)
	if p3 != '*':
		proteinlength3 += 1
	elif p3 == '*':
		if proteinlength3 > 100:
			aastart3.append(start3)
			idx3.append(len(proteinstop3))
		proteinstop3.append(int(i/3))
		proteinlength3 = 0
	protein3.append(p3)

proteinstop3.append(len(protein3) - 1)

for i in range(0, len(idx3)):
	x = idx3[i]
	a = proteinstart3[x]
	b = proteinstop3[x] + 1
	list3.append(protein3[a:b])
	str3 = ''.join(list3[i])
	seq3.append(str3)

sequences3 = {aastart3[i]: seq3[i] for i in range(len(aastart3))}
for i in idx3:
	startstop3.append([(proteinstart3[i], proteinstop3[i]), proteinstop3[i] - proteinstart3[i] + 1])

# convert protein sequences to strings and generate output
protein1 = ''.join(protein1)
protein2 = ''.join(protein2)
protein3 = ''.join(protein3)

print('\033[1m' + 'Sequences from RF1:' + '\033[0m', protein1)
print()
print(f'There are {len(idx1)} genes with proteins of more than 100 amino acids in RF1:')
print('Endpoints and Lengths of Long Proteins:', startstop1)
print(f'101+ amino-acid-sequences: {sequences1}')
print()
print('\033[1m' + 'Sequences from RF2:' + '\033[0m', protein2)
print()
print(f'There are {len(idx2)} genes with proteins of more than 100 amino acids in RF2:')
print('Endpoints and Lengths of Long Proteins:', startstop2)
print(f'101+ amino-acid-sequences: {sequences2}')
print()
print('\033[1m' + 'Sequences from RF3:' + '\033[0m', protein3)
print()
print(f'There are {len(idx3)} genes with proteins of more than 100 amino acids in RF3:')
print('Endpoints and Lengths of Long Proteins:', startstop3)
print(f'101+ amino-acid-sequences: {sequences3}')
