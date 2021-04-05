
m=int(input("enter the val "))
def fac(n):
    a=1
    for i in range(1,n+1):
        a=a*i

    print('factorial of',m,'=',a)
fac(m)