

class Triangle:
    def __init__(self):
        # User se inputs lo aur float mein convert karo
        self.side1 = float(input("Whats the length of side 1? "))
        self.side2 = float(input("What is the length of side 2? "))
        self.side3 = float(input("What is the length of side 3? "))
        
        self.perimeter = self.side1 + self.side2 + self.side3

    def display_perimeter(self):
        print("The perimeter of the triangle is", self.perimeter)


triangle = Triangle()
triangle.display_perimeter()
