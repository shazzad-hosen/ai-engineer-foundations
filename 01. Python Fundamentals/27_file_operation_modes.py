f = open("25.2_data.txt", "a")  # write and appends at the end

f.write("\nnew text being appended \nto the file.")

f.close()

# mode x -> creates a new file and open for writing
f = open("25.4_data.txt", "x")

f.write("new file created \nand data written")

f.close()

# + mode -> open any file for updation
f = open("25.2_data.txt", "r+") # write(+) and read

f.write("new data written\n")

data = f.read()
print(data)
