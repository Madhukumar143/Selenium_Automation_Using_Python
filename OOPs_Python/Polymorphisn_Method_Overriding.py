# overriding the variables and methods of parent class by creating object for child class
class A:
    a=5

    def sample_func(self):
        print("Parent class")

class B(A):
    a=10
    def sample_func(self):
        print("Child Class")

obj = B()

print(obj.a)
obj.sample_func()
