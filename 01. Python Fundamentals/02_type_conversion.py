# type conversion - automatic

first_number = 23
second_number = 46

result = second_number / first_number

print(result)
print(type(result))


# type casting
first = 33.4
second = 49

answer = int(first + second)
print(answer)

str_value = "256"
print(type(str_value))
print(type(int(str_value)))

first = 30
second = 40

result = float(first + second)
print(type(result))

value = bool(10) # false = 0; true -> any non-zero value

print(value)
print(type(value))