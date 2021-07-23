f = open("/share/SARS/SARS-2020.fasta")
genome = f.readlines()
count = {"A":0, "T":0, "G":0, "C":0}

for x in range(len(genome)):
        if x != 0:
                for i in range(len(genome[x])):
                        if genome[x][i] != "\n":
                                count[genome[x][i]] = count[genome[x][i]] + 1
print (count)
print (((count["G"] + count["C"]) / (count["A"] + count["T"] + count["G"] + count["C"])) * 100,"%")


