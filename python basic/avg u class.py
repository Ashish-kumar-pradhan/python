
class student:

    school= "AIACTR"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

s1 = student(98,78,56)
s2 = student(45,72,34)

print(s1.avg())
print(s2.avg())
