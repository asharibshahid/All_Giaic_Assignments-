def add_Greeting(cls):
    def greet(self):
        return "HEllo from Decorator"
    cls.greet = greet
    return cls

@add_Greeting
class Person:
    def __init__(self, name):
        self.name = name



person = Person("zia")
print(person.greet())  