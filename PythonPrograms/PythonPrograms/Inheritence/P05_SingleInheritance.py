"""
Single Inheritance = single parent and single child
"""


class Animal:
    def m1(self):
        print("I am parent class")


class Dog(Animal):
    def m2(self):
        print("I am child class")


dog = Dog()
dog.m1()
dog.m2()
