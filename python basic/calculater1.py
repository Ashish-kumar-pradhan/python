
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

c = int(input("enter the integer "))

d = int(input("enter the integer "))

n= int(input("selet what process u want to do \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n enter the value "))
if n==1:
    add(c,d)
if n==2:
    sub(c,d)
if n==3:
    mul(c,d)
if n==4:
    div(c,d)
elif n>4:
    print("your input for selecting the operation is wrong \n try it again ")
elif n<1:
    print("your input for selecting the operation is wrong \n try it again ")