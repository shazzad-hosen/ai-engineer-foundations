numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # tuples are immutable sequence of values

print(numbers)
print(type(numbers))

print(len(numbers))
print(numbers[4]) # index 4

# we can't assign items in a tuple
# numbers[3] = 10 - it will throw error
print(numbers[3])

# typles with different types of data
person = ("Shazzad Hosen", 21, "Developer", 3.7)
print(person)

# creating a single value tuple
number = (1, ) # we must put a comma

print(type(number))
print(number)


# slicing in a tuple
marks = (81, 82, 83, 84, 85, 86)

print(marks[0 : 3]) # ending index not included
print(marks) # slicing doesn't harm to original tuple items

print(marks[2 :]) # index 2 to last index


# tuple methods
nums = (79, 81, 63, 67, 83, 93, 93, 81, 67, 57, 90, 84, 67)

print(f"index of first occurance is: {nums.index(67)}")
print(f"count of occurance is: {nums.count(81)}")




# loops in a tuple
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

for i in tup:
    print(i)