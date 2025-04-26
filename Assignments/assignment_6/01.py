class Students:
    def __init__(self, Fullname , marks):
        self.name = Fullname
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


s1 = Students("Ali" , 90)
s2 = Students("Sara" , 85)

s1.display()

