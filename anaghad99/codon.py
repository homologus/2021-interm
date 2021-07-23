
codon_table = {"TTT":"F", "TTC": "F", "TTA": "F", "TTG":"F", "CTT":"L", "CTC":"L", "CTA":"L","CTG":"L","ATT":"I","ATC":"I","ATA":"I","ATG":"M","GTT":"V","GTC":"V","GTA":"V","GTG":"V", "TCT":"S","TCC":"S","TCA":"S","TCG":"S","CCT":"P","CCC":"P","CCA":"P","CCG":"P","ACT":"T","ACC":"T","ACA":"T","ACG":"T","GCT":"A","GCC":"A","GCA":"A","GCG":"A", "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*","CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","AAT":"N","AAC":"N","AAA":"K","AAG":"K","GAT":"D","GAC":"D","GAA":"E","GAG":"E","TGT":"C","TGC":"C","TGA":"*","TGG":"W","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGT":"S","AGC":"S","AGA":"R","AGG":"R","GGT":"G","GGC":"G","GGA":"G","GGG":"G"}
file = open('nucl.fasta')
lines = file.readlines()
lines.pop(0)

og_sequence = ''.join(lines)
og_sequence = og_sequence.replace('\n', '')
og_sequence_2 = og_sequence[1:]

print(og_sequence)

def remove_first_n_char(og_str, n):
	mod_string = ""
	for i in range(n, len(og_str)):
		mod_string = mod_string + og_str[i]
	return mod_string


og_sequence_4 = remove_first_n_char(og_sequence, 2)

def split_sequence(sequence):
	splits = 3
	list_of_splits = [(sequence[i:i+splits]) for i in range(0, len(sequence), splits)]
	return list_of_splits


def split_sequence_2(sequence): #this one splits the sequence from the second character

	
	splits = 3
	list_of_splits = [(sequence[i:i+splits]) for i in range(0, len(sequence), splits)]
	return list_of_splits




sequence_list_inthree = split_sequence(og_sequence)


#sequence_list_inthree_starttwo = split_sequence_2(og_sequence_2)
#sequence_list_inthree_startthree = split_sequence(og_sequence_4)

for i in sequence_list_inthree:
	for key in codon_table:
		if key == i:
			og_sequence = og_sequence.replace(i, codon_table.get(i))

#for i in sequence_list_inthree_starttwo:
#	for key in codon_table:
#		if key == i:
#			og_sequence_2 = og_sequence_2.replace(i, codon_table.get(i))

#for i in sequence_list_inthree_startthree:
#	for key in codon_table:
#		if key == i:
#			og_sequence_4 = og_sequence_4.replace(i, codon_table.get(i))

#print(og_sequence)



#print(og_sequence)
#print(og_sequence_2)
#print(og_sequence_4)
