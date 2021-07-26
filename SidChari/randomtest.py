import random

x=float(input("GC Content should be:"))
y=int(input("Total length should be:"))

x_decimal=x/100
z=int((y*x_decimal)//1)
list=[]

for i in range(0, z//2):
    list.append("G")
    list.append("C")

for i in range(z//2, y//2):
    list.append("A")
    list.append("T")

print(len(list))

count_g=list.count("G")
count_c=list.count("C")
gc_content=100*(count_g+count_c)/len(list)

print(f"{gc_content}%")

random.shuffle(list)
seqstr=''.join(list)

