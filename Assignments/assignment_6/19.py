class Multipilier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number
    

Res = Multipilier(12)
print(callable(Res))  

result = Res(5)
print(result)  