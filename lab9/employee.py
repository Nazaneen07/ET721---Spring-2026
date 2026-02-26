"""
Nazaneen Baguaei,
lab 9, unit testing
feb 26, 2026
"""
class Employee:
    # property
    raise_amt = 1.05

    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary 

    @property 
    def emailemployee(self):
        return f"{self.first}_{self.last}@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"  # fixed: "f{...}" → f"{...}" (missing f-string prefix)
    
    # method
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

"""
# local testing 
# create instance of the class 
employee = Employee("Peter", "Pan", 80000)
print(f"employee = {employee.fullname}")
print(f"employee email = ${employee.emailemployee}")      
print(f"employee salary = ${employee.salary} per year")   
employee.apply_raise()                                    
print(f"employee salary after the raise = ${employee.salary}") 


"""