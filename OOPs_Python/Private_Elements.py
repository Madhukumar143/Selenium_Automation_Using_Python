#Private variables and private methods

class One :
    __a= 5  #Creating Private Variable
    def __Sample_One(self): #private Method
        print("Inside Sample One Class")

    def Private_Variable_Access(self):
        print(self.__a)
        self.__Sample_One()


obj = One()

obj.Private_Variable_Access()


