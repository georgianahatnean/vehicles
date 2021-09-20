class Person:
    def __init__(self, first_name, family_name, age, country):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
        self.country = country

    def details(self):
        print(" My name is ", self.first_name, self.family_name)
        print(" I am " + self.age + " years old and i am from ", self.country)

