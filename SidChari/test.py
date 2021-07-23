import Bio
from Bio.Seq import Seq

x=str(input())
seqx=Seq(x)
print(seqx)
revcomp=seqx.reverse_complement()
print(revcomp)
