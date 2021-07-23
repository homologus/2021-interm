
f=open('/share/SARS/SARS-2020.fasta', 'r')
genome = f.readlines()
count = {"A":0,"T":0,"C":0,"G":0}

for i in range(len(genome)):
    if i != 0:
        for x in range(len(genome[i])):
            if genome[i][x] != "\n":
                count[genome[i][x]] += 1
print(count)
print((count['G']+count['C'])/( count["A"]+count["T"]+count["C"]+count["G"])*100)
