from Bio import SeqIO
from Bio.Seq import Seq

inp=str(input("Input file name:"))
reads = list(SeqIO.parse(inp, "fasta"))
#sequence=Seq(inp)

###takes reads, outputs combined sequence from all records in reads

def sqnc(x):
    for i in range(len(x)):
        seqstr=""
        temp=x[i].seq
        strtemp=str(temp)
        seqstr=seqstr+strtemp
    sequence=Seq(seqstr)
    return sequence

###takes sequence, trims to multiple of 3, converts to type Bio.Seq.Seq

def trim(sequence):
    liszt=list(sequence)
    while len(liszt)%3 != 0:
        del liszt[-1]
        continue
    seqstring=''.join(liszt)
    sequence=Seq(seqstring)
    return sequence

###takes sequence, creates reverse complement

def revcom(sequence):
    return sequence.reverse_complement()

###creates 3 reading frames from sequence
sequence=sqnc(reads)

liszt2=list(sequence)
del liszt2[0]
rf2=''.join(liszt2)
del liszt2[0]
rf3=''.join(liszt2)

###creates 3 reading frames from reverse complement

rc=revcom(sequence)
rc_list=list(rc)
del rc_list[0]
rc_rf2=''.join(rc_list)
del rc_list[0]
rc_rf3=''.join(rc_list)

###trims all reading frames

sequence=trim(sequence)
rf2=trim(rf2)
rf3=trim(rf3)
rc=trim(rc)
rc_rf2=trim(rc_rf2)
rc_rf3=trim(rc_rf3)

###find proteins greater than 100 amino acids long

translate1=sequence.translate()
translate2=rf2.translate()
translate3=rf3.translate()
translate4=rc.translate()
translate5=rc_rf2.translate()
translate6=rc_rf3.translate()

def protein(x):
    liszt3=[]
    for i in range(len(x)):
        if x[i]=="*":
            liszt3.append(i)
    return liszt3

def findlong(x):
    list4=[]
    for i in range(len(x)-1):
        var_1=x[i]
        var_2=x[i+1]
        if var_2-var_1>100:
            list4.append(i)
    return list4

protein1=protein(translate1)
findlong1=findlong(protein1)

protein2=protein(translate2)
findlong2=findlong(protein2)

protein3=protein(translate3)
findlong3=findlong(protein3)

protein4=protein(translate4)
findlong4=findlong(protein4)

protein5=protein(translate5)
findlong5=findlong(protein5)

protein6=protein(translate6)
findlong6=findlong(protein6)


def protlist(findlong1, protein1, translate1):
    list5=[]
    for i in findlong1:
        temp1=protein1[i]+1
        temp2=protein1[i+1]+1
        strtrans=str(translate1)
        tempseq=strtrans[temp1:temp2]
        list5.append(tempseq)
    return list5

def protloc(findlong1, protein1):
    startstop=[]
    for i in findlong1:
        temp1=protein1[i]+1
        temp2=protein1[i+1]
        startstop.append(f"{temp1}:{temp2}")
    return startstop

protlist1=protlist(findlong1, protein1, translate1)
protlist2=protlist(findlong2, protein2, translate2)
protlist3=protlist(findlong3, protein3, translate3)
protlist4=protlist(findlong4, protein4, translate4)
protlist5=protlist(findlong5, protein5, translate5)
protlist6=protlist(findlong6, protein6, translate6)

protloc1=protloc(findlong1, protein1)
protloc2=protloc(findlong2, protein2)
protloc3=protloc(findlong3, protein3)
protloc4=protloc(findlong4, protein4)
protloc5=protloc(findlong5, protein5)
protloc6=protloc(findlong6, protein6)


###prints full translations, proteins greater than 100aa with locations

print("Sequence Translations:")
print("Reading frame 1 is:", sequence.translate())
print("Reading frame 2 is:", rf2.translate())
print("Reading frame 3 is:", rf3.translate())
print()
print("Reverse Complement Translations:")
print("Reading frame 4 is:", rc.translate())
print("Reading frame 5 is:", rc_rf2.translate())
print("Reading frame 6 is:", rc_rf3.translate())

print()

print(f"Proteins greater than 100 amino acids in reading frame 1 are: {protlist1} at {protloc1}")
print(f"Proteins greater than 100 amino acids in reading frame 2 are: {protlist2} at {protloc2}")
print(f"Proteins greater than 100 amino acids in reading frame 3 are: {protlist3} at {protloc3}")
print(f"Proteins greater than 100 amino acids in reading frame 4 are: {protlist4} at {protloc4}")
print(f"Proteins greater than 100 amino acids in reading frame 5 are: {protlist5} at {protloc5}")
print(f"Proteins greater than 100 amino acids in reading frame 6 are: {protlist6} at {protloc6}")





