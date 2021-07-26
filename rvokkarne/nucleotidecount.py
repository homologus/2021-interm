import re

file = str(input("File name: "))
f = open(file, 'r')
lines = f.readlines()

title_re = re.compile('>(\S+)')
notitle_re = re.compile('^(\S+)')

total_count = 0
nucleotide_count = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
gc_content = 0

DNAseq_str = []

for line in lines:
	outh = title_re.search(line)
	if outh:
		continue
	else:
		outl = notitle_re.search(line)
		outm = outl.group(1)
		DNAseq = list(outm)
		DNAseq_str += DNAseq

for i in range(1, len(DNAseq_str)+1):
	total_count += 1

for i in DNAseq_str:
	nucleotide_count[i] += 1

gc_content = ((nucleotide_count['G'] + nucleotide_count['C'])/total_count)*100

print(nucleotide_count)
print('GC content: ',gc_content)
print('Total: ',total_count)
