class car:
    #static Variable
    wheels = 4
    def __init__(self,brand,model,price, milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage

    def Start_car(self):
        print(self.brand+"car having model as "+self.model+" has not started")

    #static class can access only static variables/methods that to using class name only not with self key word
    @staticmethod
    def Print_Car_Wheels():
        print(car.wheels)

    @staticmethod
    def demo_Static():
        car.Print_Car_Wheels()
        #instance methods and variables can be used in static methods as below
        car_3 = car("Honda ","CBZ",1000000,17)
        car_3.Start_car()

car_1 = car("Benz","Mercedeez",1500000,15)
car_2 = car("BMW ","G330",2000000,8)

print(car.wheels)
car_1.Start_car()
car_2.Start_car()
car_1.demo_Static()
