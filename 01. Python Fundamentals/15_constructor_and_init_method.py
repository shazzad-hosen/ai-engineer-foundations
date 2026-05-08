# we can only have a single constructor in a class
class Student:
    # constructor function
    def __init__(self): # self -> refrence to the current object
        print("constructor was called...")
        
# every time we creates an object constructor function is being called
student1 = Student()
student1 = Student()
student1 = Student()


# custom methods in a class
class Person:
    def __init__(self, name, age): # parameterized constructor
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, {self.name}")
        
person1 = Person("Jisan", 19)
person2 = Person("Shazzad", 21)

print(person1.name, person1.age)
print(person2.name, person2.age)

# calling greet method for objects
person1.greet()
person2.greet()