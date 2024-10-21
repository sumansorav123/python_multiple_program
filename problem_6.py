# create a class "employee" and ddd salery and increment properties to it . 

class Employee:
    salary = 250 
    increment = 20

    @property
    def incremented_salary(self):
        return self.salary + (self.salary * self.increment / 100)

    @incremented_salary.setter
    def incremented_salary(self, new_salary):
        # Calculate new increment based on the new salary
        self.increment = (new_salary - self.salary) / self.salary * 100

# Creating an instance of the Employee class
e = Employee()
e.incremented_salary = 300  # Set the incremented salary to 300
print(f'Original Salary: {e.salary}')
print(f'Increment: {e.increment}%')
print(f'Incremented Salary: {e.incremented_salary}')