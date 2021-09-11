"""
Lecture: 310
parent class members are default available to child class and we can access from child class using child reference
But if constructors, variable, methods are same in both parent and child class then super function is used to access
or call parent class method, constructor and variables
"""


class P:
    def m1(self):
        print("I am Parent class m1 method")


class C(P):
    def m1(self):
        # self.m1() # it will call child class m1 and recurssion error will comw on lin number 8
        super().m1()# it will call parent class m1 method
        print("I am child class m1 method")


c = C()
c.m1()
