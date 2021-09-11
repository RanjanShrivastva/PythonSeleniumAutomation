class P:
    def __init__(self):
        print("I am parent class constructor")
        self.b = 10

    def m1(self):
        print("I am parent class instance method")

    @classmethod
    def m2(cls):
        print("I am parent's class class method")

    @staticmethod
    def m3():
        print("I am parent class static method")


class C(P):
    pass


c = C()
c.m1()
c.m2()
c.m3()
