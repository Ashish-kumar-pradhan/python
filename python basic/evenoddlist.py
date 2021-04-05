lst=list()

n=int(input("enter the number of element in list"))

for j in range(n):
    x=int(input("enter elements"))
    lst.append(x)

print(lst)

def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

even,odd = count(lst)
print("even:{} and odd : {} ".format(even,odd))