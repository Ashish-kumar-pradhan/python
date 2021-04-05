m=int(input("enter the how long fibonacci sequence u want "))
def fib(n):
    a=0
    b=1
    if n==1:
        print(0)
    elif n<=0:
        print(" invalid input \n there is no sequence  ")
    else :
        print(0)
        print(1)
        for i in range(2,n):
              c=a+b
              a=b
              b=c
              print(c)

fib(m)