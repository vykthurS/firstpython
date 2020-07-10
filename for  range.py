a=5
b=6
c=12
tot=0
for i in range(b,c):
    resto= i % a
    if (resto >=2):
        tot=tot+i
print ("o valor de tot é:", tot)
