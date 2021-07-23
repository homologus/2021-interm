import sys, re

x=str(input("Input genome file name:"))
#seqstr=list(x)
f=open(x, 'r')
lines=f.readlines()

hre=re.compile('>(\S+)')
lre=re.compile('^(\S+)')

test=0
string=''

for line in lines:
	outh = hre.search(line)
	if outh:
		continue
	else:
		string=string+line
		if test%10000==0:
		    print(test)
		test+=1

#string=''.join(seqstr)

count=0
indices=[]
regex=re.compile("GAC.....GTC")

for i in range(0, len(string)):
    temp=string[i:i+11]
    if len(temp)<11:
        break
    check=regex.search(temp)
    if check:
        indices.append(count+6)
    if i%10000 == 0:
        print(i)
    count+=1

indices.insert(0, 0)
indices.append(len(string))
parts = [string[indices[i]:indices[i+1]] for i in range(0, len(indices)-1)]

number_of_parts=(len(parts))
length_of_parts=[]

for i in parts:
    length_of_parts.append(len(i))

print(f"Number of parts: {number_of_parts}")
print(f"Length(s) of parts: {length_of_parts}")
