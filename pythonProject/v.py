class Person:
    def __init__(self, first_name, family_name, age, country):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
        self.country = country

    def details(self):
        print("My name is ", self.first_name, self.family_name)
        print("I am " + self.age + " years old and i am from ", self.country)

class Vehicles:
    def __init__(self, v_type, mark, year, colour, gearbox, fuel_type, price):
        self.v_type = v_type
        self.mark = mark
        self.year = year
        self.colour = colour
        self.gearbox = gearbox
        self.fuel_type = fuel_type
        self.price = price

    def ceva(self):
        print("your " + self.v_type + " is a " + str(self.year), self.mark + " from , the colour is " + self.colour)
        print("the gearbox is: " + self.gearbox + " and the fuel type is: " + self.fuel_type)
        print("the car price is: " + str(self.price))


def paymethod(value):
    pay = int(input("how do you want to pay?"
                    "1-cash"
                    "2-debit card"
                    "3-credit card"))
    if pay == 1:
        print("Congratulations on the purchase")
    elif pay == 2:
        print("Congratulations on the purchase")
    elif pay == 3:
        nr = int(input("the number of installments you want to pay: "))
        print("the value of a installment: ", value/nr)
        r = int(input("Do you want to change the payment method?"
                      "1-YES"
                      "2-NO"))
        if r == 1:
            paymethod(value)
    else:
        print("Unknown payment method")

g = open('peoples_data.txt', 'r')
z = g.readlines()
for element in z:
    w = element.split()
    first_name, family_name, age, country = w
    people = Person(first_name, family_name, age, country)
    people.details()
    f = open('vehicles_data.txt', 'r')
    x = f.readlines()
    ok = 0
    while ok==0:
        for item in x:
            y = item.split()
            v_type, mark, year, colour, gearbox, fuel_type, price = y
            vehicle = Vehicles(v_type, mark, year, colour, gearbox, fuel_type, price)
            vehicle.ceva()
            mes=int(input("do you want this vehicle? " 
                          "1-YES " 
                          "2-NO : "))
            if mes==1:
                ok=1
                break
    f.close()
g.close()