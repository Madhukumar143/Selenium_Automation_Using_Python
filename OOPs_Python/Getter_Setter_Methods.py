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