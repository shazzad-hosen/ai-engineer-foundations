# multi level inheritance
class Employee:
    start_time = "9AM"
    end_time = "1PM"


class AdminStuff(Employee):
    def __init__(self, role):
        self.role = role


class Accountant(AdminStuff):
    def __init__(self, salary, role):
        super().__init__(role)  # calling constructor of the parent class to pass role
        self.salary = salary


acc1 = Accountant(125_000, "CA")
print(acc1.start_time, acc1.end_time, acc1.salary, acc1.role)


# multiple inheritance
class Teacher:
    def __init__(self, salary):
        self.salary = salary


class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa


class TA(Teacher, Student):
    def __init__(self, salary, cgpa, name):
        super().__init__(salary)
        Student.__init__(self, cgpa)

        self.name = name


ta1 = TA(25_000, 3.7, "shazzad_hosen")
print(ta1.name, ta1.cgpa, ta1.salary)
