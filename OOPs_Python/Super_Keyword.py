#Accessing or calling the parent class properties from child class which are having the same name as child properties

# Without using Super() keyword
'''class A:
    a = 3
    def Sample(self):
        print("Method inside class A")

class B(A):
    a = 4
    def Sample(self):
        print("Method inside Class B")

    def Print_Properties(self):
        print(self.a)
        self.Sample()

Obj_B = B()
Obj_B.Print_Properties()'''

# By using Super() Keyword

class A():
    def __init__(self):
        print("init method inside class A")
    def Super_test(self):
        print("testing Super keyword")

class B(A):
    def __init__(self):
        super().Super_test()
        print("init method inside class B")

B()
