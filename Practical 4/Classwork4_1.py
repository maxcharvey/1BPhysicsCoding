class Vehicle:

    description = 'A thing used for transport'

    def __init__(self, manufacturer, topspeed):
        self.manufacturer = manufacturer
        self.topspeed = topspeed

    def printbasicinfo(self):
        print("\nThe vehicle is manufactured by " + self.manufacturer + '.')
        print("It has a top speed of: " + str(self.topspeed) + ',')


class Car(Vehicle):

    description = "A 4 wheeled road vehicle"

    def __init__(self, manufacturer, topspeed, nopassengers, boot):
        super().__init__(manufacturer, topspeed)
        self.manufacturer = manufacturer
        self.topSpeed = topspeed
        self.nopassengers = nopassengers
        self.boot = boot

    def printcarinfo(self):
        self.printbasicinfo()
        print("The number of passengers that the car can transport is "+str(self.nopassengers))

        if self.boot:
            print("This car has a boot")
        else:
            print("this car does not have a boot")

    @classmethod
    def overwritedescription(cls, newdescription):
        cls.description = newdescription

    @staticmethod
    def turnonradio(station):
        print("\nThe ratio is runed on an playing the " + station + "station")

    def __add__(self, other):
        newmanufacturer = self.manufacturer + "-" + other.manufacturer + '-Tron'
        newtopspeed = max(self.topspeed, other.topspeed)*1.2
        newnopassengers = self.nopassengers + other.nopassengers
        newboot = (self.boot or other.boot)
        return Car(newmanufacturer, newtopspeed, newnopassengers, newboot)


normalCar = Car('McMorris', 150, 4, True)
bootlessCar = Car('LandRover', 200, 2, False)

normalCar.printbasicinfo()
bootlessCar.printbasicinfo()
normalCar.printcarinfo()