class Person:
    def __init__(self , name ):
        self.name = name
        print(f"Person Constructor Called")

class Teacher(Person):
    def __init__(self , name , subject ):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher Constructor Called")        

result = Teacher("Arif" , "Urdu")
print(result.name)        
print(result.subject)