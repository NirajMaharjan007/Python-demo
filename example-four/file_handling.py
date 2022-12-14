f = open("example-four/file.txt", "r")

print()
'''
    f.read(5) => parameter shows size
    f.readLine()
    f.readLines()
'''
print(f.read())

print()

file_append = open("example-four/file.txt", "a")
file_append.write("\nHello")

# w means overwrite the files
# file_write = open("example-four/file.txt", "w")
# file_write.write("")
