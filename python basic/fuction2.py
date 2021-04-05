
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('ashish',age=20,city='delhi')
