class Car:
    brand: str = "BMW"
    
    def Start(self):
        print(f"{self.brand} is starting")







cr1 = Car()
Car.Start(cr1)
print(cr1.brand)