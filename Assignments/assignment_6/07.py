class Employee:
    def __init__(self, name, salary , ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
        
res = Employee("Ali" , 10000 , 123456789)
print(res.name)
print(res._salary)        
# print(res.__ssn) # Error
# now we have a task which is how to access ssn hmmm
print("Private SSN Via Name Manglind:", res._Employee__ssn)