color = str(input("color: "))

if color == "red":
    print("stop!")
    
elif color == "green":
    print("go!")
    
elif color == "yellow":
    print("look!")
    
else:
    print("wrong color for trafic lights!")
    
    
# excercise 01
username = str(input("username: "))    
password = str(input("password: "))

if (username == "admin" and password == "passwordOne"):
    print("Access granted")
    
elif (username != "admin"):
    print("Wrong username")
    
else: 
    print("Wrong password")    
    

# excercise 02
number = int(input("enter number: "))

if (number % 2 == 0):
    print("even number")
    
else:
    print("odd number")


# nesting in conditional statements
username = str(input("username: "))
password = str(input("password: "))

if (username == "admin" and password == "passOne"):
    print("login successful")
    
else:
    if (username != "admin"):
        print("wrong username")
        
    else: 
        print("wrong password")
        
# match case
colour = str(input("colour: "))

match colour:
    case "Green":
        print("Go")
        
    case "Red":
        print("Stop")
        
    case "Yellow":
        print("Look")
    
    # this is default case
    case _:
        print("wrong colour")