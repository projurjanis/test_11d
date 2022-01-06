import math

garums=float(input("ievadi: "))

l1=math.pow(garums,2)
l2=math.pow(garums+5,2)

proc=l2/l1

print(str((proc*100)-100) + "%")
