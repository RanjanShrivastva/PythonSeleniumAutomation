class A:
    def m1(self):
        print("I am A class m1 method")


class B(A):
    def m1(self):
        print("I am B class m1 method")


class C(B):
    def m1(self):
        print("I am C class m1 method")


class D(C):
    def m1(self):
        print("I am D class m1 method")


class E(D):
    def m1(self):
        super().m1()  # it will call immediate super class method of current class
        C.m1(self)  # it will call C class m1 method from E class
        super(B, self).m1()  # it will call immediate super class  m1 method as A is immediate supper class of B
        # print("I am E class m1 method")


e = E()
e.m1()
