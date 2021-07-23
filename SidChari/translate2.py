import sys, re

x=str(input("Input genome file name:"))
seqstr=list(x)

codona = {"AAA":'K', "AAT":'N', "AAG":'K', "AAC":'N', "ATA":'I', "ATT":'I', "ATG":'M', "ATC":'I', "AGA":'R', "AGT":'S', "AGG":'R', "AGC":'S', "ACA":'T', "ACT":'T', "ACG":'T', "ACC":'T'}
codont = {"TAA":'*', "TAT":'Y', "TAG":'*', "TAC":'Y', "TTA":'L', "TTT":'F', "TTG":'L', "TTC":'F', "TGA":'*', "TGT":'C', "TGG":'W', "TGC":'C', "TCA":'S', "TCT":'S', "TCG":'S', "TCC":'S'}    
codong = {"GAA":'E', "GAT":'D', "GAG":'E', "GAC":'D', "GTA":'V', "GTT":'V', "GTG":'V', "GTC":'V', "GGA":'G', "GGT":'G', "GGG":'G', "GGC":'G', "GCA":'A', "GCT":'A', "GCG":'A', "GCC":'A'}
codonc = {"CAA":'Q', "CAT":'H', "CAG":'Q', "CAC":'H', "CTA":'L', "CTT":'L', "CTG":'L', "CTC":'L', "CGA":'R', "CGT":'R', "CGG":'R', "CGC":'R', "CCA":'P', "CCT":'P', "CCG":'P', "CCC":'P'}

R_codons = {"CGT":0, "CGA":0, "CGG":0, "CGC":0, "AGA":0, "AGG":0}
R_codons_temp = {"CGT":0, "CGA":0, "CGG":0, "CGC":0, "AGA":0, "AGG":0}

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
pstop=[]
count=[]

for i in range(0, len(seqstr)-2, 3):
  temp=[]
  temp=temp+seqstr[i:i+3]
  if len(temp)<3:
    break
  strtemp = ''.join(temp)
  cod=codon[strtemp]
  if cod=="R":
    R_codons_temp[strtemp]+=1
  if plength==0:
    start=int(i/3)
    pstart.append(int(i/3))
  if cod != "*":
    plength = plength+1
  elif cod == "*":
    if plength >= 100:
       for key in R_codons_temp:
         R_temp=R_codons_temp[key]
         R_codons[key]=R_codons[key]+R_temp
       aaloc.append(start)
       count.append(len(pstop))
    for key in R_codons_temp:
       R_codons_temp[key]=0
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
  dictionary3={y:z}
  fred.append(sequence[y:z+1])
  franz=fred[i]
  franzstr=''.join(franz)
  franzliszt.append(franzstr)

dictionary={aaloc[i]: franzliszt[i] for i in range(len(aaloc))}

dictionary2={pstart[i]:pstop[i] for i in count}
#var=[]
#for i in count:
#  var=sequence[pstart[count[i]]:pstop[count[i]]]

#for i in range(0, len(seqstr)-2, 3):
#  temp2=[]
#  temp2=temp2+seqstr[i+1:i+4]
#  if len(temp2)<3:
#    break
#  strtemp2 = ''.join(temp2)
#  cod2=codon[strtemp2]
#  plength2=0
#  if plength2==0:
#    start2=i+1
#  if cod2 != "*":
#    plength2 += 1
#  elif cod2 == "*" and plength2 >= 100:
#    aaloc2.append(start2)
#  sequence2.append(cod2)

#for i in range(0, len(seqstr)-2, 3):
#  temp3=[]
#  temp3=temp3+seqstr[i+2:i+5]
#  if len(temp3)<3:
#    break
#  strtemp3 = ''.join(temp3)
#  cod3=codon[strtemp3]
#  plength3=0
#  if plength3==0:
#    start3=i+2
#  if cod3 != "*":
#    plength3 += 1
#  elif cod3 == "*" and plength3 >= 100:
#    aaloc3.append(start3)
#  sequence3.append(cod3)

seqstr2 = ''.join(sequence)
#seqstr3 = ''.join(sequence2)
#seqstr4 = ''.join(sequence3) 

print("reading frame 1 is", seqstr2)
print()
#print("reading frame 2 is", seqstr3)
print()
#print("reading frame 3 is", seqstr4)

print()
print("Proteins of length greater than or equal to 100 amino acids:")
print(f"{dictionary} in reading frame 1")
print(R_codons)
#print(dictionary)
#print(f"{aaloc2} in reading frame 2")
#print(f"{aaloc3} in reading frame 3")
sys.exit() 
