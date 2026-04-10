print("Hello World \nFrom Python")

name = "Shazzad Hosen"
print("Hello,", name)
print("Hello, " + name)

age = 21
print(age)
print("I am, ", age - 2)

job = "developer"
print(name, age, job)

cgpa = "good"
print(cgpa)

# dynamically type allocation
cgpa = 3.6
print(cgpa)

# true is True in python *_*
is_good = True
none = None # no value

# type function in action
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_good))
print(type(none))
print(type("Hello"))

'''
I am
multi-line
comment
'''

# arithmetic operators
first_number = 199
second_number = 211

print(first_number + second_number)
print(2 * 2)
print(8 / 2)

print(2 ** 3) # a to the power b
print(9 % 2) # calculate remainder


# relational operators - return boolean results
print(first_number == second_number)
print(second_number > first_number)


# assignment operator
value = 100
value += 20
value -= 100
value **= 2

print(value)


# logical operator
is_good = False

print(not is_good)
print(not (5 < 3))
print(not (""))
print(not (" "))

print(is_good and (5 > 4))

print(is_good or True)