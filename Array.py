from array  import *
vals=array('i',[1,2,3,4,5])
print(vals)
newarray=array(vals.typecode,(a for a in vals))

for i in range(1,5):
    print (newarray[i])
print("Index of "+str(vals.index(5)))