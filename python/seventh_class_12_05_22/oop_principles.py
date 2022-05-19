# oop principles = 1. Abstraction, 2. Encapsulation, 3. Inheritance, 4. Polymorphism
from abstruction_example import Student


class StudentImpl(Student):
    # properties => variable/attr/instance, function- custom function, builtin function
    # encapsulation -> private( __ ), protected ( _ ), public
    # Inheritance -> multilevel inheritance, multiple inheritance

    # global variable
    # __name = ""
    # __dept = ""

    # constructor
    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept

    def getName(self):
        return self.__name

    def getDept(self):
        return self.__dept

    def setName(self, name):
        self.__name = name

    def setDept(self, dept):
        self.__dept = dept

    def getSemister(self, ):
        sem = "6th"
        return sem

    def __str__(self, ):
        return "Student name {}, his/her dept {}".format(self.__name, self.__dept)


# student = StudentImpl('Tamim', 'CSE')
# student2 = StudentImpl('Shamim', 'BBA')
# print(student)
# print(student2)
# print(student.name)