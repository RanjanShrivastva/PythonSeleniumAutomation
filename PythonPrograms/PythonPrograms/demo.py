class Student:  # Class
    school_name = 'Albert High School'  # Static Variable

    def __init__(self, name, roll_no):      # Constructor
        self.name = name    # Instance Variable
        self.roll_no = roll_no  # Instance Variable

    def get_student_info(self):     # Instance Method
        print("Student Name : ", self.name)
        print("Roll no : ", self.roll_no)

    @classmethod    # Class Method
    def get_school_name(cls):
        print("School Name : ", cls.school_name)

    @staticmethod   # Static Method
    def get_sum(a, b):
        print("Sum of {} and {} is ".format(a, b, a+b))


#   Function call
st = Student("Amit", 100)
st.get_student_info()
st.get_school_name()
Student.get_sum(100, 200)


