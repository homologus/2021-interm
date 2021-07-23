r =open("/share/SARS/SARS-2020.fasta")
g = r.readlines()

table={'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L', 'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
'TAT':'Y','TAC':'Y','TAA':'STOP', 'TAG':'STOP', 'TGT':'C', 'TGC':'C', 'TGA':'STOP', 'TGG':'W',
'CTT':'L','CTC':'L','CTA':'L','CTG':'L','CCT':'P','CCC':'P','CCA':'P','CCG':'P','CAT':'H',
'CAC':'H','CAA':'Q','CAG':'Q','CGT':'R','CGC':'R','CGA':'R','CGG':'R','GTC':'V',
'ATT':'I','ATC':'I','ATA':'I','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T',
'AAT':'N','AAC':'N','AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R',
'GTT':'V','GTG':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
'GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGC':'G','GGA':'G','GGG':'G'}

convert1 = ''
convert2 = ''
convert3 = ''

for f in range(1,len(g)):
    line = g[f]
    line = line[:-2]
    for i in range(len(line)-2):
        if(i%3) == 0:
            convert1 += table[line[i:i+3]]
    for i in range(len(line)-2):
        if(i%3) == 1:
            convert2 += table[line[i:i+3]]
    for i in range(len(line)-2):
        if(i%3) == 2:
            convert3 += table[line[i:i+3]]
print(convert1,"END of convert one")
print(convert2,"END of convert two")
print(convert3,"END of convert three")


