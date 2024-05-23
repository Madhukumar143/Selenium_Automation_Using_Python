'''class Parent:

    def First_method(self):
        print("First_Method")

    def First_Method(self,a):
        print("in Second method" , a)

obj = Parent())
# it will take the latest created Method
obj.First_Method(4)'''
#Method Overloading can be achieved as below
class A:
    def Sample(self,a=0,b=0):
        if (a!=0) and (b!=0) :
            print(a+b)
        elif  a!= 0 :
            print(a)
        elif b!= 0:
            print(b)
        else:
            print("Nothing")

object = A()
#object.Sample(2)
#object.Sample(3,5)
