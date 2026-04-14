def print_hello():
    print("Hello, Function")
    
print_hello()
print_hello()


def add_numbers(first, second):
    return first + second

print("sum is:", add_numbers(10, 6))


# default values
def calculate_average(a, b = 8):
    return (a + b) / 2

print("average is:", calculate_average(10))
print(calculate_average) # observation


# lambda function -> only have a single expression
sum = lambda x, y, z: (x + y +z)

print("sum:", sum(99, 12, 13))
print(sum) # observation


# factorial calculator
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        
    return factorial

n = int(input("Enter a number: "))
print(calculate_factorial(n))