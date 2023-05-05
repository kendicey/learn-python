class A:
    def a(self):
        return "Function inside A"


class B:
    def a(self):
        return "Function inside B"


# left to right, search in A first, then search in B
class C(A, B):
    def b(self):
        return "Function inside C"
    pass


class D(C):
    pass


d = D()
# d is an instance of D, which is an instance of C
print(d.b())  # Function inside C
