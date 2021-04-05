
def sub(a,b):
    c=a-b
    print("subtraction= ",c)

def div(a, b):
    c= a / b
    print("division= ",c)

def sqr(a):
    c=a*a
    print("square of",a," = ",c)

def cube(a):
    c=a*a*a
    print("cube of",a," = ",c)

def sqrt(a):
    c=a**(1/2)
    print("squareroot of",a," = ",c)

def cbrt(a):
    c=a**(1/3)
    print("cuberoot of",a," = ",c)

n=int(input("selet what process u want to do \n 1 for addition            2 for multiplication \n 3 for subtraction         4 for division \n 5 for square              6 for cube \n 7 for square root         8 for cube root \n enter the value "))
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
if 0<n<3:
     if n == 1:
         lst = list()
         n = int(input("enter the number of element you want to add "))

         for j in range(n):
             x = int(input("enter element "))
             lst.append(x)

         print( "sum=",sum(lst))

     if n == 2:
         lst = list()

         n = int(input("enter the number of element you want to multiply "))

         for j in range(n):
             x = int(input("enter element "))
             lst.append(x)
         a = 1
         for i in range(n):
             a = a * lst[i]
         print("multiplication=",a)

if 0<n<5:
    a = int(input("enter the first integer "))
    b = int(input("enter the second integer "))

    if n == 3:
        sub(a, b)

    if n == 4:
        div(a, b)

elif n<0:
    print(" your input for selecting the operation is wrong \n please select a number between 1 to 8 \n try it again ")

elif n>8:
    print(" your input for selecting the operation is wrong \n please select a number between 1 to 8 \n try it again ")