from vehicles_class import Vehicles
from peoples_class import Person
def paymethod(value):
    pay = int(input(" how do you want to pay? "
                    " 1-cash "
                    " 2-debit card "
                    " 3-credit card "))
    if pay == 1:
        print(" Congratulations on the purchase ")
    elif pay == 2:
        print(" Congratulations on the purchase ")
    elif pay == 3:
        nr = int(input(" the number of installments you want to pay: "))
        print(" the value of a installment: ", int(value)/nr)
        r = int(input(" Do you want to change the payment method? "
                      " 1-YES "
                      " 2-NO "))
        if r == 1:
            paymethod(value)
    else:
        print(" Unknown payment method ")

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
    while ok == 0:
        for item in x:
            y = item.split()
            v_type, mark, year, colour, gearbox, fuel_type, price = y
            vehicle = Vehicles(v_type, mark, year, colour, gearbox, fuel_type, price)
            vehicle.setmark("h")
            print(vehicle.getmark)
            vehicle.ceva()
            mes = int(input("do you want this vehicle? " 
                          " 1-YES " 
                          " 2-NO : "))
            if mes == 1:
                ok = 1
                paymethod(price)
                break
    f.close()
    print("--------------------------------------------------------")
g.close()
