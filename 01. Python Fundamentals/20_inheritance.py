# base class
class Employee:
    start_time = "10am"
    end_time = "3PM"

    def change_end_time(self, new_end_time):
        self.end_time = new_end_time


# derived class
class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


t1 = Teacher("Math")
t1.change_end_time("3:30PM")
print(t1.subject, t1.start_time, t1.end_time)
