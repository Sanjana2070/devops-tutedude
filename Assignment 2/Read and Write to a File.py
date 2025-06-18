<<<<<<< HEAD
# Write to a File
with open("output.txt", "w") as file:
    file.write("This is a sample content written to a file.\n")
    file.write("File I/O is easy in Python!\n")
print("Content written to 'output.txt'")

# Read from a File
try:
    with open("output.txt", "r") as file:
        content = file.read()
        print("\nContents of the file:")
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
=======
# Write to a File
with open("output.txt", "w") as file:
    file.write("This is a sample content written to a file.\n")
    file.write("File I/O is easy in Python!\n")
print("Content written to 'output.txt'")

# Read from a File
try:
    with open("output.txt", "r") as file:
        content = file.read()
        print("\nContents of the file:")
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
>>>>>>> af418ba (Assignment 5)
