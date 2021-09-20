class Vehicles:
    def __init__(self, v_type, mark, year, colour, gearbox, fuel_type, price):
        self.v_type = v_type
        self.mark = mark
        self.year = year
        self.colour = colour
        self.gearbox = gearbox
        self.fuel_type = fuel_type
        self.price = price
        self.__mark = mark

    def ceva(self):
        print(" your " + self.v_type + " is a " + str(self.mark), self.year + " the colour is " + self.colour)
        print(" the gearbox is: " + self.gearbox + " and the fuel type is: " + self.fuel_type)
        print(" the car price is: " + str(self.price))

    def getmark(self):
        return self.__mark

    def setmark(self,m):
        self.__mark=m