
codon_table = {"TTT":"F","TTC":"F","TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L",
"CTG":"L","ATT":"I","ATC":"I","ATA":"I","ATG":"M","GTT":"V","GTC":"V","GTA":"V",
"GTG":"V","TCT":"S","TCC":"S","TCA":"S","TCG":"S","CCT":"P","CCC":"P","CCA":"P","CCG":"P",
"ACT":"T","ACC":"T","ACA":"T","ACG":"T","GCT":"A","GCC":"A","GCA":"A","GCG":"A","TAT":"Y",
"TAC":"Y","TAA":"*","TAG":"*","CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","AAT":"N","AAC":"N",
"AAA":"K","AAG":"K","GAT":"D","GAC":"D","GAA":"E","GAG":"E","TGT":"C","TGC":"C", "TGA":"*",
"TGG":"W","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGT":"S","AGC":"S","AGA":"R","AGG":"R",
"GGT":"G","GGC":"G","GGA":"G","GGG":"G"}

file = open('nucl.fasta')
lines = file.readlines()
lines.pop(0)

og_sequence = ''.join(lines)
og_sequence = og_sequence.replace('\n', "")
og_sequence_2 = og_sequence[1:]





def split_sequence(sequence):
	splits = 3
	list_of_splits = [(sequence[i:i+splits]) for i in range(0, len(sequence), splits)]
	return list_of_splits

def remove_first_n_char(og_str, n):
	mod_string = ""
	for i in range(n, len(og_str)):
		mod_string = mod_string + og_str[i]
	return mod_string



og_sequence_3 = remove_first_n_char(og_sequence, 2)

sequence_list_inthree = split_sequence(og_sequence)
#print(sequence_list_inthree)
sequence_list_inthree_frametwo = split_sequence(og_sequence_2)
sequence_list_inthree_framethree = split_sequence(og_sequence_3)

for i in sequence_list_inthree:
	for key in codon_table:
		if key == i:
			print(i, codon_table.get(i))

for i in sequence_list_inthree_frametwo:
	for key in codon_table:
		if key == i:
			print(i, codon_table.get(i))

for i in sequence_list_inthree_framethree:
	for key in codon_table:
		if key == i:
			print(i, codon_table.get(i))
