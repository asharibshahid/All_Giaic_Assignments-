
class Counter:
    count = 0 
    def __init__(self):
        Counter.count += 1
    @classmethod
    def show_Count(cls):
        print(f"The Object Count Is {cls.count}")  


objec1 = Counter()
objec2 = Counter()

Counter.show_Count()
