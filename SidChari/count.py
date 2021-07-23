import sys, re

x=str(input("Input genome file name:"))
f=open(x, 'r')
lines=f.readlines()

hre=re.compile('>(\S+)')
lre=re.compile('^(\S+)')

A=0
T=0
G=0
C=0

for line in lines:
	outh = hre.search(line)
	if outh:
		continue
	else:
		outl=lre.search(line)
		outm=outl.group(1)
		liszt=list(outm)
		A+=liszt.count("A")
		T+=liszt.count("T")
		G+=liszt.count("G")
		C+=liszt.count("C")
print()
print(A, "As")
print(T, "Ts")
print(G, "Gs")
print(C, "Cs")
print()

#GC Content
GC=G+C
total=A+T+G+C
gc_content = float(GC/total)
gccpercent=gc_content*100

print(f"total nucleotide count is: {total}")
print(f"GC Content is: {gccpercent}%")

