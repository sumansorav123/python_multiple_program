# write  a class " calculator " capable of finding sqare , cube and square root of no .

# take the user input
# The class Calculator takes a user input number, and provides methods to calculate the square, cube,
# and square root of that number.

while True:
    try:
        num = int(input("Enter the number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a inter number.")
        exit()

class Calculator:
    
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num * self.num}")
    
    def cube(self):
        print(f"The cube of {self.num} is {self.num ** 3}")
    
    def square_root(self):
        print(f"The square root of {self.num} is {self.num ** 0.5}")

# Creating an instance of Calculator with user input
cal = Calculator(num)

# Calling the square method
cal.square()
cal.cube()
cal.square_root()