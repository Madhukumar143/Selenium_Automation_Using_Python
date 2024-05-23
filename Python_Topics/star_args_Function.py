def sample(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

sample(name="Madhu",experience=3,Location="Nellore")

def sample(*live):
    for k in live:
        print(k,end=" ")

sample(1,2,3,6)
print()
def employee(name,experience,location):
    print(name, experience,location)

m = {"name":"Madhu", "experience":3,"location":"Nellore"}

employee(**m)