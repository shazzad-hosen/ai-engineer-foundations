f = open("25.2_data.txt", "w")

# it will truncate the file first
f.write("text to overwrite \nthe complete data")

f.close()