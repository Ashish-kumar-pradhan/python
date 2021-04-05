
from array import *

arr = array('i',[])

n=int(input('enter the number of elements in array '))

for i in range(n):
    x=int(input("enter the value "))
    arr.append(x)

print(arr)

val= int(input("enter the value u want to search "))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1

