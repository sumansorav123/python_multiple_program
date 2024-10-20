# create a class "twovector " and use it to create another class represent threedvector 

# Parent class
class twoVector:
    # declare the constructor
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    # declare the method to show the vector
    def show(self):
        print(f"The two vector is {self.i}i + {self.j}j")

# Child class 
# inherit the parent class
class threeVector(twoVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    # declare the method to show the vector
    def show(self):
        print(f"The three vector is {self.i}i + {self.j}j + {self.k}k")

# Create instances and call methods
vector1 = twoVector(2, 3)
vector1.show()  # prints: The two vector is 2i + 3j

vector2 = threeVector(2, 3, 4)
vector2.show()  # prints: The three vector is 2i + 3j + 4k