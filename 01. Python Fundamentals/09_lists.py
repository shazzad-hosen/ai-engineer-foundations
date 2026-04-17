marks = [81, 83, 87, 89, 97, 91, 93] # list is the mutable sequence of values

print(marks)
print(type(marks))

print(marks[6]) # index
print(len(marks))

marks[1] = 85 # list item's are mutable
print(marks)
print(marks[1])

# slicing in a list
print(marks[0 : 4]) # ending index is not included

print(marks) # slicing doesn't harm to the original list items

person = ["Shazzad Hosen", 21, "programmer", True]
print(person)
print(type(person))


# list methods
heroes = ["Iron Man", "Batman", "Super-man"]

print(heroes)
print(len(heroes))

heroes.append("Flash") # add one element at the end of the list
print(heroes)
print(len(heroes))


heroes.insert(2, "Thor") # add new element to a specific index
print(heroes)
print(len(heroes))

numbers = [7, 5, 8, 4, 9, 2, 1, 3, 6]

numbers.sort() # sort number is increasing order
print(numbers)

numbers.sort(reverse=True) # decreasing order sorting
print(numbers)

numbers.reverse() # reverse 
print(numbers)


# loops with lists
numbers = [12, 10, 7, 9, 3, 5, 1]

numbers.sort()

for i in numbers:
    print(i)
    
print("after first loop")
    
for i in range(0, len(numbers)):
    print(numbers[i])
  

# linear search with list and loop  
values = [3, 7, 5, 1, 3, 2, 8, 9]

target = 8
index = 0


for i in values:
    if (i == target):
        print(f"{target} found at index: {index}")
        break
    index += 1
