# This is a mechanism Which wraps the data (variables (data),  and Methods(Code)) together under a single unit
#Binding the data to the class, By Making the Variables as private and accessing them only via non-private methods 9getter and Setter methods)

# To Access private variables and methods outside the class
class One:

    __Age = 22

    def Set_Age(selfself,Age):
        One.__Age = Age

    def Get_Age(selfself):
        return  One.__Age


obj = One()
obj.Set_Age(24)
print(obj.Get_Age())