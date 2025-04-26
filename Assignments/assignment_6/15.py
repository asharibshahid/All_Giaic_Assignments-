class A:
    def Show(self):
        print("Show from A")

class B(A):
    def Show(self):
        print("Show from B")

class C(A):  
    def Show(self):              
        print("Show From C")

class D(B,C):
    pass


d = D()
d.Show()

print(D.__mro__)


