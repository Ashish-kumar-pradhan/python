lst=list()

n=int(input("enter the number of element in list"))

for j in range(n):
    x=input("enter elements")
    lst.append(x)

print(lst)

def count(lst):
    gt=0
    lt=0

    for i in lst:
        i=0
        i+=1
        if len(lst[i])>=4:
            gt+=1
        else:
            lt+=1

    return gt,lt

gt,lt = count(lst)
print("gt:{} and lt : {} ".format(gt,lt))