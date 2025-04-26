class Counter:
    def __init__(self , Start):
        self.current = Start
        print("Counter Created")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result
    

for number in Counter(7):
    print(number)    