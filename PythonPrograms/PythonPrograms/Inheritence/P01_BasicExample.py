class P:
    def m1(self):
        print("I am parent class")


class C(P):
    def m2(self):
        print("I am child class")


# function call
c = C()
c.m1()
c.m2()
