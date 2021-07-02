from Bio import SeqIO
reads = list(SeqIO.parse("aldh2-human", "fasta"))
output = open("mutatedexon12", "w")

sequence = reads[0].seq

exon12 = ''
for i in range(len(sequence)):
	if i == 1510:
		exon12 += 'A'
	else:
		exon12 += sequence[i]

output.write(exon12)
