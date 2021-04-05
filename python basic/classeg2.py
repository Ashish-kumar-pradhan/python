
class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config is ",self.cpu,self.ram)

comp1=computer("i5",16)
comp2=computer("ryzen 5 ",8)

comp1.config()
comp2.config()