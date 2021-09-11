class Car:
    def __init__(self, cname, cmodel, ccolor):
        self.cname = cname
        self.cmodel = cmodel
        self.ccolor = ccolor

    def car_info(self):
        print("Car name: {} \t\n Car model is: {} \t\n Car color is: {}".format(self.cname, self.cmodel, self.ccolor))


class Person:
    def __init__(self, ename, eage):
        self.ename = ename
        self.eage = eage

    def eat(self):
        print(self.ename, " is eating biryani..")


class Employee(Person):
    def __init__(self, ename, eage, eno, esal, car):
        super().__init__(ename, eage)
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print(self.ename, " is doing python coding")

    def emp_info(self):
        print("Employee name is : ", self.ename)
        print("Employee age is : ", self.eage)
        print("Employee number is : ", self.eno)
        print("Employee salary is : ", self.esal)
        print("Car Information")
        self.car.car_info()


car = Car("Nexon", 2021, "Blue")
e = Employee("Ranjan", 29, 2414, 20000, car)
e.eat()
e.work()
e.emp_info()
