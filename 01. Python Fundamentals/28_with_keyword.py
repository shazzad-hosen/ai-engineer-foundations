# with -> automatically close file after operations
with open("25.4_data.txt", "r") as f:
    data = f.read()
    print(data)