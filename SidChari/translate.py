import sys, re, Bio
from Bio.Seq import Seq

x=str(input("Input genome file name:"))
f=open(x, 'r')
lines=f.readlines()

hre=re.compile('>(\S+)')
lre=re.compile('^(\S+)')

#seqst = []
seqstr = []

for line in lines:
	outh = hre.search(line)
	if outh:
		continue
	else:
		outl=lre.search(line)
		outm=outl.group(1)
		liszt=list(outm)
#		seqst = seqst+liszt
		seqstr=seqstr+liszt

#strrev=''.join(seqst)
#dnaseq=Seq(strrev)
#revcomp=dnaseq.reverse_complement()
#seqstr=list(revcomp)

codona = {"AAA":'K', "AAT":'N', "AAG":'K', "AAC":'N', "ATA":'I', "ATT":'I', "ATG":'M', "ATC":'I', "AGA":'R', "AGT":'S', "AGG":'R', "AGC":'S', "ACA":'T', "ACT":'T', "ACG":'T', "ACC":'T'}
codont = {"TAA":'*', "TAT":'Y', "TAG":'*', "TAC":'Y', "TTA":'L', "TTT":'F', "TTG":'L', "TTC":'F', "TGA":'*', "TGT":'C', "TGG":'W', "TGC":'C', "TCA":'S', "TCT":'S', "TCG":'S', "TCC":'S'}    
codong = {"GAA":'E', "GAT":'D', "GAG":'E', "GAC":'D', "GTA":'V', "GTT":'V', "GTG":'V', "GTC":'V', "GGA":'G', "GGT":'G', "GGG":'G', "GGC":'G', "GCA":'A', "GCT":'A', "GCG":'A', "GCC":'A'}
codonc = {"CAA":'Q', "CAT":'H', "CAG":'Q', "CAC":'H', "CTA":'L', "CTT":'L', "CTG":'L', "CTC":'L', "CGA":'R', "CGT":'R', "CGG":'R', "CGC":'R', "CCA":'P', "CCT":'P', "CCG":'P', "CCC":'P'}

codona.update(codont)
codona.update(codong)
codona.update(codonc)
codon = codona

sequence = []
sequence2 = []
sequence3 = []
aaloc = []
aaloc2 = []
aaloc3 = []
plength=0
plength2=0
plength3=0
start=0
start2=0
start3=0
pstart=[]
pstart2=[]
pstart3=[]
pstop=[]
pstop2=[]
pstop3=[]
count=[]
count2=[]
count3=[]

for i in range(0, len(seqstr)-2, 3):
  temp=[]
  temp=temp+seqstr[i:i+3]
  if len(temp)<3:
    break
  strtemp = ''.join(temp)
  cod=codon[strtemp]
  if plength==0:
    start=int(i/3)
    pstart.append(int(i/3))
  if cod != "*":
    plength = plength+1
  elif cod == "*":
    if plength >= 100:
       aaloc.append(start)
       count.append(len(pstop))
    pstop.append(int(i/3))
    plength=0
  sequence.append(cod)

pstop.append(len(sequence)-1)
fred=[]
franzliszt=[]
for i in range(0, len(count)):
  x=count[i]
  y=pstart[x]
  z=pstop[x]
  fred.append(sequence[y:z+1])
  franz=fred[i]
  franzstr=''.join(franz)
  franzliszt.append(franzstr)

dictionary={aaloc[i]: franzliszt[i] for i in range(len(aaloc))}
startstop={pstart[i]:pstop[i] for i in count}

for i in range(0, len(seqstr)-2, 3):
  temp2=[]
  temp2=temp2+seqstr[i+1:i+4]
  if len(temp2)<3:
    break
  strtemp2 = ''.join(temp2)
  cod2=codon[strtemp2]
  if plength2==0:
    start2=int(i/3)
    pstart2.append(int(i/3))
  if cod2 != "*":
    plength2 = plength2+1
  elif cod2 == "*":
    if plength2 >= 100:
       aaloc2.append(start2)
       count2.append(len(pstop2))
    pstop2.append(int(i/3))
    plength2=0
  sequence2.append(cod2)

pstop2.append(len(sequence2)-1)
fred2=[]
franzliszt2=[]
for i in range(0, len(count2)):
  x=count2[i]
  y=pstart2[x]
  z=pstop2[x]
  fred2.append(sequence2[y:z+1])
  franz2=fred2[i]
  franzstr2=''.join(franz2)
  franzliszt2.append(franzstr2)

dictionary2={aaloc2[i]: franzliszt2[i] for i in range(len(aaloc2))}
startstop2={pstart2[i]:pstop2[i] for i in count2}


for i in range(0, len(seqstr)-2, 3):
  temp3=[]
  temp3=temp3+seqstr[i+2:i+5]
  if len(temp3)<3:
    break
  strtemp3 = ''.join(temp3)
  cod3=codon[strtemp3]
  if plength3==0:
    start3=int(i/3)
    pstart3.append(int(i/3))
  if cod3 != "*":
    plength3 = plength3+1
  elif cod3 == "*":
    if plength3 >= 100:
       aaloc3.append(start3)
       count3.append(len(pstop3))
    pstop3.append(int(i/3))
    plength3=0
  sequence3.append(cod3)

pstop3.append(len(sequence3)-1)
fred3=[]
franzliszt3=[]
for i in range(0, len(count3)):
  x=count3[i]
  y=pstart3[x]
  z=pstop3[x]
  fred3.append(sequence3[y:z+1])
  franz3=fred3[i]
  franzstr3=''.join(franz3)
  franzliszt3.append(franzstr3)

dictionary3={aaloc3[i]: franzliszt3[i] for i in range(len(aaloc3))}
startstop3={pstart3[i]:pstop3[i] for i in count3}


seqstr2 = ''.join(sequence)
seqstr3 = ''.join(sequence2)
seqstr4 = ''.join(sequence3) 

print("reading frame 1 is", seqstr2)
print()
print("reading frame 2 is", seqstr3)
print()
print("reading frame 3 is", seqstr4)

print()
print("Proteins of length greater than or equal to 100 amino acids at:")
print(f"{dictionary} in reading frame 1")
print(f"start:stop at {startstop}")
print(f"{dictionary2} in reading frame 2")
print(f"start:stop at {startstop2}")
print(f"{dictionary3} in reading frame 3")
print(f"start:stop at {startstop3}")

sys.exit() 
