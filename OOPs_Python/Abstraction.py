#methods which are defined and without implimentation or method body are called Abstract methods
#you can not create object for Abstract class directly
# We can Acces the Abstract class methods and variables only if we overload all the abstarct methods of abstract class in child class and then we can create object for child class and acces the methods in abstract class
#Constructors can be created in abstract Class

from abc import ABC, abstractmethod
class One(ABC):

    def __init__(self,a):
        self.a = a

    @abstractmethod  #Abstract method
    def method_One(self):
        print("Abstraction method")
        pass

    @abstractmethod  # Abstract method
    def method_Two(self):
        print("Abstraction method")
        pass

    def method_Three(self):#Non-Abstract method
        print("inside method Three")
        print(self.a)

class Two(One):
    def method_One(self):
        print("abstract method inside Abstract class overloaded here")
    def method_Four(self):
        print("method inside Child class")

class Three(Two):
    def method_Two(self):
        print("abstract method inside Abstract class overloaded here")
    def method_Five(self):
        print("method inside Child class")
obj =Three(18)

obj.method_One()
obj.method_Two()
obj.method_Three()
obj.method_Four()
obj.method_Five()

