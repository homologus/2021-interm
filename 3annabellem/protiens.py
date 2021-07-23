f = open("/share/SARS/SARS-2020.fasta")
g = f.readlines()
T0 = []
T1 = []
T2 = []

table =  {'TTT':'F','TTC':'F','TTA':'L','TTG':'L','TCT':'S','TCC':'S','TCA':'S','TCG':'S',
'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','TGT':'C','TGC':'C','TGA':'*','TGG':'W','CTT':'L',
'CTC':'L','CTA':'L','CTG':'L','CCT':'P','CCC':'P','CCA':'P','CCG':'P','CAT':'H','CAC':'H',
'CAA':'Q','CAG':'Q','CGT':'R','CGC':'R','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ATA':'I',
'ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T','AAT':'N','AAC':'N','AAA':'K','AAG':'K',
'AGT':'S','AGC':'S','AGA':'R','AGG':'R','GTT':'V','GTG':'V','GTA':'V','GTG':'V','GCT':'A',
'GCC':'A','GCA':'A','GCG':'A','GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G',
'GGC':'G','GGA':'G','GGG':'G','GTC':'V'}

for x in range(len(g)):
	if x != 0:
		g[x] = g[x][0:-1] 
		for i in range(len(g[x])-2):
			if i%3 == 0:
		  		T0 = T0 + [table[g[x][i:i+3]]]

		for i in range(len(g[x])-2):
			if i%3 == 1:
		        	T1 = T1 + [table[g[x][i:i+3]]]

		for i in range(len(g[x])-2):
			if i%3 == 2:
		        	T2 = T2 + [table[g[x][i:i+3]]]

def str (list):
	list_final = ''
	for i in range(len(list)):
		list_final = list_final + list[i]
	return list_final


print(str(T0))
print(str(T1))
print(str(T2))
