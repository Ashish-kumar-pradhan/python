
from array import *

arr = array('i',[])

n=int(input('enter the number of elements in array '))

for i in range(n):
    x=int(input("enter the value"))
    arr.append(x)
print(arr)
arr.reverse()
print("the reverse array is")
print(arr)