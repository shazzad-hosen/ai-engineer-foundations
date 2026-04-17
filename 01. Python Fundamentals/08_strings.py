name = "Shazzad Hosen" # strings are immutable in python

print(name)
print(len(name)) # length of the sequence
print(name[0]) # index

first_name = "Jisan"
last_name = "Ahmed"

full_name = first_name + " " + last_name # string concatenation
print(full_name)

# loop on a string
for i in full_name:
    print(i)
    
    
# string operations
string = "python"

print(string[2 : 4]) # ending index not included

new_str = string[2 : 4]
print(new_str)

print(string[2:]) # 2 to end of the string

print(string) # slicing doesn't harm to the original string


# string formatting
first = 20
second = 30

sum = first + second

print("sum is: {}".format(sum)) # format function
print("sum of {} and {} is: {}".format(first, second, sum))

print("sum of {1} and {0} is: {2}".format(first, second, sum)) # index based formatting
print("sum of {first} and {second} is: {sum}".format(first = 10, second = 8, sum = 18)) # value based formatting

print("love language is {}".format("python"))


# string formatting using f-string
print(f"sum of {first} and {second} is: {sum}") # f-string => literal interpolation
print(f"average of {first} and {second} is: {(first + second) / 2}")