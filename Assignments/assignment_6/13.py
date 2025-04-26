class Engine:
    def start(self):
        print("Engine Started: ...")

class Car:
    def __init__(self,engine):
        self.engine = engine
        print("Car Created")

    def start_Car(self):
        self.engine.start()
        print("Car Started")


my_engine = Engine()
my_car = Car(my_engine)
print(my_car.start_Car())