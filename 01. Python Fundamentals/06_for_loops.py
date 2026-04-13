string = "Shazzad Hosen"

for i in string: # in -> membership operator
    print(i)
    
 
# in operator: check presences
string = "abcdefghij"

if ("l" in string):
    print("exists")
    
else:
    print("doesn't exists")
    

# another type of for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8] # list 
n = 5

for i in range(0, n): # loop will iterate through index (0 to n - 1)
    print(numbers[i])
    
print("outside of the loop...")


# range function: generate sequences -> (start, stop(must), step)
for i in range(1, 10, 2):
    print(i)


# vowel count problem
word = "artificial"
count = 0

for letter in word:
    if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        count += 1
        
print("vowel's are: ", count)


# sum of first nth number
number = int(input("Number: "))
sum = 0

for i in range(1, number + 1):
    sum += i
    
print("sum is: ", sum)