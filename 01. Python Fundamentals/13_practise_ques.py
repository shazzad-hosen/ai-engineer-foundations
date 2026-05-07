# group all unique courses
info = [
    ("Tom", "Physics"),
    ("Alice", "English"),
    ("Bob", "Math"),
    ("Kenny", "Chemistry"),
    ("Alice", "Botany"),
    ("Charlie", "Math"),
    ("Tom", "Chemistry"),
    ("Bob", "Statistics")
]

unique_courses = set()

for name, course in info:
    unique_courses.add(course)

print(unique_courses)


# list students enrolled in Math
students_set = set()

for students in info:
    if (students[1] == "Math"):
        students_set.add(students[0])
        
print(students_set)
 

# create dictionary (student, set of courses)
dict = {}

for name, course in info:
    if (dict.get(name) == None):
        dict.update({ name: set()})
        dict[name].add(course)    
    else:
        dict[name].add(course)
print(dict)
        