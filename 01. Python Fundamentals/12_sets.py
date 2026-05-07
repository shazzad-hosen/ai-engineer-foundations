# set is a collection of unique immutable elements. but set it self can be mutable
nums = { 1, 2, 3, 4, 5, 6, 3, 4, 5, 1, 2 } # set doesn't store duplicate values

print(type(nums))
print(len(nums))
print(nums)

# set itself a mutable data type
nums.add(7)

print(nums)
print(len(nums))

# empty set
empty_set = set() # set() is a constructor function it self

print(type(empty_set))
print(len(empty_set))
print(empty_set)

empty_set.add(1)
print(empty_set)


# set methods
marks = { 98, 96, 93, 92, 91, 90, 89 }
print(marks)
print(type(marks))

# add method, adds a new element at the last
marks.add(88)
print(marks)

# remove methd, removes a specefic element
marks.remove(96)
print(marks)

# pop method removes a random value
marks.pop()
print(marks)


s1 = { 1, 2, 3, 4, 5 }
s2 = { 4, 5, 6, 7, 8 }

# intersection method filters common elements
common = s1.intersection(s2)
print(common)

# union method filters all unique elements
all_unique = s1.union(s2)
print(all_unique)
