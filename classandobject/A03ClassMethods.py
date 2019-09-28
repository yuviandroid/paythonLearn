

'''class A:

    div = "D"

    def __init__(self):
        self.name = "ABCD"

    def f1(self): # object as a first parameter in instance method
        print(f"f1 instance method is called name is {self.name}")

    @staticmethod
    def f2(name):
        print(f"f1 static method is called name is {name}")

    @classmethod
    def f3(cls):    # class as a first parameter
        print(f"f3 class method is called name is {cls.div}")


a1 =A()
a1.f1()     # instance method
# A.f1(a1)
A.f3()      # class method
a1.f3()
A.f2("Yuvraj")  # Static method '''

class Arithmatic:

    mul_num = 5

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    @classmethod
    def mul(cls,x):
        return x * cls.mul_num

    @staticmethod
    def div(p,q):
        return p//q


a1 = Arithmatic(20,10)
a2 = Arithmatic(2,3)

print(a1.add())
print(a2.add())

print(Arithmatic.mul(10))
print(Arithmatic.div(6,3))