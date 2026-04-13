counter = 1
while (counter < 15):
    print("Hello World")
    counter += 1
       
i = 0
while(i < 20):
    print(i)
    i += 1

# infinite loop
# while True:
#     print("I am a infinite loop")

# 01: multiplication table
number = int(input("Enter a number: "))

iterator = 1
while(iterator <= 10):
    print(iterator * number)
    iterator += 1
    
# break and continue keyword
i = 1
while(i < 10):
    if (i == 7):
        break
    
    print(i)
    i = i + 1

print("after break")

i = 1
while(i <= 10):
    if (i % 2 == 0): # skip multiples of 3
        i += 1 # important 
        continue
    
    print(i)
    i += 1
    
print("outside loop...")