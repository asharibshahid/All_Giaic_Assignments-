class Employee:
    def __init__(self , name ):
        self.name = name
        
    def get_info(self):
        return  f"The employee name is {self.name}"
    


class Deparment(Employee):
     def __init(self,dept_name,employee):
         self.dept_name = dept_name
         self.employee = employee

     def show_Details(self):
        return f"Department Name: {self.dept_name}, Employee Info: {self.employee.get_info()}"         
     
emp = Employee("Asharib")
dept = Deparment("HR", emp)     
print(dept.show_Details())