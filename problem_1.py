# create a class " programmer " for storing the information of new employe working at microsoft

class Programmer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

# Creating an object of the Programmer class
c = Programmer("Suman", 9500000)

# Calling the display method
c.display()

c = Programmer("Sorav", 9500000)

# Calling the display method
c.display()