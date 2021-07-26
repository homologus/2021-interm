import sys, re

file = str(input("File: "))
f = open(file, 'r')
lines = f.readlines()

title_re = re.compile('>(\S+)')
notitle_re = re.compile('^(\S+)')

progress = 0
DNAseq = ''

for line in lines:
        outh = title_re.search(line)
        if outh:
                continue
        else:
                DNAseq += line

sites = []
restrictionsites = {1: 0}
count = 1
sitecount = 0
lengths = {}
number = 0
regex = re.compile('GAC.....GTC')

for i in range(0, len(DNAseq)):
	temp = DNAseq[i:i+11]
	if len(temp) < 11:
		break
	test = regex.search(temp)
	if test:
		count += 1
		restrictionsites[count] = i+6
		sites.append(i+6)

sites.insert(0, 0)
sites.append(len(DNAseq))
for i in range(len(sites) - 1):
	segment = DNAseq[sites[i]:sites[i+1]]
	sitecount += 1
	lengths[i+1] = len(segment)

print()
print(f'There are {sitecount} segments.')
print()
print('These are the indices of the restriction sites:', restrictionsites)
print()
print('These are the lengths of each segment (as numbered above):', lengths)
