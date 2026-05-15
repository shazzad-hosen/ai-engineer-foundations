class Student:
    college_name = "ABC college of Engineering" # class attributes -> common to all objects
    
    def __init__(self, name, age):
        self.name = name # instance attributes
        self.age = age
        
student1 = Student("Jisan", 21)

# accessing instance attributes
print(student1.name)

# accessing class attributes, both are valid
print(student1.college_name)
print(Student.college_name)
