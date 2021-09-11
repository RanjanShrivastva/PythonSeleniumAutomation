"""
Hierarchical Inheritance = One parent but multiple child classes and all child classes are at sam level.
P = Parent
C = Child
GC  = Grand Child
"""


class P:
    def m1(self):
        print("I am parent class")


class C1(P):
    def m2(self):
        print("I am child-1 class")


class C2(P):
    def m3(self):
        print("I am Child-2 Class")


c1 = C1()
c1.m1()
c1.m2()
c2 = C2()
c2.m1()
c2.m3()

