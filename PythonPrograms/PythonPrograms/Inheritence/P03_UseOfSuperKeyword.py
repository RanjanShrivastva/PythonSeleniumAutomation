class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("Eating Chicken Biryani ")


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def work(self):
        print("python coding")

    def emp_info(self):
        print("Employee name is: ", self.name)
        print("Employee age is: ", self.age)
        print("Employee number is: ", self.eno)
        print("Employee salary is: ", self.esal)


e = Employee("Ranjan", 32, 24141, 2000)
e.emp_info()
e.work()
e.eat()





