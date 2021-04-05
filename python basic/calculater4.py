
def add(a,b):
    c=a+b
    print(c)

def sub(a,b):
    c=a-b
    print(c)

def mul(a, b):
    c = a * b
    print(c)

def div(a, b):
    c= a / b
    print(c)

def sqr(a):
    c=a*a
    print(c)

def cube(a):
    c=a*a*a
    print(c)

def sqrt(a):
    c=a**(1/2)
    print(c)

def cbrt(a):
    c=a**(1/3)
    print(c)



n=int(input("selet what process u want to do \n 1 for addition            2 for subtraction \n 3 for multiplication      4 for division \n 5 for square              6 for cube \n 7 for square root         8 for cube root \n enter the value "))
if 4<n<9:
     a = int(input("enter the integer "))
     if n==5:
          sqr(a)
     if n==6:
          cube(a)
     if n == 7:
         sqrt(a)
     if n == 8:
         cbrt(a)

elif 0<n<5:
    a = int(input("enter the first integer "))
    b = int(input("enter the second integer "))
    if n == 1:
        add(a, b)
    if n == 2:
        sub(a, b)
    if n == 3:
        mul(a, b)
    if n == 4:
        div(a, b)

else:
    print("your input for selecting the operation is wrong \n try it again ")

