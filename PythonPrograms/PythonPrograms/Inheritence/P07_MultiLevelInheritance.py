"""
MultiLevel Inheritance = multiple levels of Inheritance
P = Parent
C = Child
GC  = Grand Child
"""


class P:
    def m1(self):
        print("I am parent class")


class C(P):
    def m2(self):
        print("I am child class")


class GC(C):
    def m3(self):
        print("I am Grand Child Class")


gc = GC()
gc.m1()
gc.m2()
gc.m3()
