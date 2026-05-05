# dictionary stores data in a key value pair - key's must be unique

student = {
    "name": "Shazzad Hosen",
    "age": 21,
    "dept": "Physics",
    "courses": ["mechanics", "waves and oscilations", "thermodynamics"],
    "cgpa": 3.7,
    "isGood": True
}

print(student)
print(type(student))

print(student["courses"])
print(type(student["courses"]))


info = {
    "name": "Jisan Ahmed",
    "age": 19,
    "profession": "AI Engineer"
}
print(info)

# dictionary is mutable and unordered
info["name"] = "Shazzad Hosen"
print(info)


# we can use any type of keys we want
science = {
    3.14: "PI",
    9.81: "gravitational acceleration"  
}
print(science[9.81])


# dictionary methods
data = {
    "format": "json",
    "size": "100GB",
    "origin": "world-wide",
}

print(len(data))

# returns keys of a dictionary
print(data.keys())

dict_keys = list(data.keys())
print(f"list of keys: {dict_keys}")

# returns values of a dictionary
print(data.values())

# returns key-value pairs of a dictionary
print(data.items())

# returns value of a key. if key is invalid retruns None
print(data.get("siz")) # None
print(data.get("size"))

# update method to insert new item in a dictionary
data.update({
    "datapoint": "1M",
    "type": "user_data"
})

print(data)
print(len(data))