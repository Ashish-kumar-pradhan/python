
def fv(u,a,t):
    v=u+a*t
    print("final velocity is ",v,"m/s")

def iv(v,a,t):
    u=v-a*t
    print("initial velocity is ",u,"m/s")

def ac(u, v, t):
    a=(v-u)/t
    print("acceleration is ", a, "m/s2")

def tm(u,a,v):
    t=(v-u)/a
    print("time taken is ",t,"s")

n=int(input("select what you want to find \n 1 for final velocity \n 2 for initial velocity \n 3 for acceleration \n 4 for time \n enter.. "))

if n==1:
    u = int(input("enter initial velocity in m/s "))
    a = int(input("enter acceleration in m/s2 "))
    t = int(input("enter time taken in s "))
    fv(u,a,t)

if n==2:
    v = int(input("enter final velocity in m/s "))
    a = int(input("enter acceleration in m/s2 "))
    t = int(input("enter time taken in s "))
    iv(v,a,t)

if n==3:
    u = int(input("enter initial velocity in m/s "))
    v = int(input("enter final velocity in m/s "))
    t = int(input("enter time taken in s "))
    ac(u,v,t)

if n==4:
    u = int(input("enter initial velocity in m/s "))
    a = int(input("enter acceleration in m/s2 "))
    v = int(input("enter final velocity in m/s "))
    tm(u,a,v)

if n>4:
    print("your choice is wrong \nplease run again")
if n<1:
    print("your choice is wrong \nplease run again")