"""
Hybrid Inheritance = Combination of Single, Multiple, Multilevel, Hierarchical
Symbol : 'Y' with Inverted 'Y'
    | |
     |
    | |
P_ = Parent
C = Child
GC  = Grand Child

In Hybrid Inheritance method resolution is based on MRO Algorithm
"""


class P1:
    def m1(self):
        print("I am parent-1 class")


class P2:
    def m1(self):
        print("I am Parent-2 class")


class C(P1, P2):
    def m2(self):
        print("I am Child Class")

# Order of argument matters based on order child class method will be called
# if methods are same in parent and child class then priority goes to child class first then
# class C(P2, P1):
#     def m2(self):
#         print("I am Child Class")


c = C()
c.m1()
c.m2()
# c.m3()

