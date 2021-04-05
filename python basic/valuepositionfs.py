
m=int(input("enter the position in fibonacci sequence "))
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(b)
    else :
        for i in range(2,n):
              c=a+b
              a=b
              b=c
        print('value of position',m,'=',c)

fib(m)