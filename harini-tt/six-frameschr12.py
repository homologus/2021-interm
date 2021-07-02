from Bio import SeqIO
reads1 = list(SeqIO.parse("aldh2-human", "fasta"))
sequence = reads1[0]
reads2 = list(SeqIO.parse("mutatedexon12", "fasta"))
mutSequence = reads2[0]

# regular sequence
frame1 = sequence.translate()
print(frame1)

oneLessSeq = sequence[1:len(sequence)-1]
frame2 = oneLessSeq.translate()
print(frame2)

twoLessSeq = sequence[2:len(sequence)-1]
frame3 = twoLessSeq.translate()
print(frame3)

# mutated sequence
frame4 = mutSequence.translate()
print(frame4)

oneLessSeqM = mutSequence[1:len(mutSequence)-1]
frame5 = oneLessSeqM.translate()
print(frame5)

twoLessSeqM = mutSequence[2:len(mutSequence)-1]
frame6 = twoLessSeqM.translate()
print(frame6)
