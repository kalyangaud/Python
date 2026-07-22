filename= "ABC.txt"
with open(filename, "w") as file:
    file.write("Hello, Welcome to Python File Handling.\n")
    file.write("This is the second line.\n")
print("Data written successfully.\n")
print("Contents of the file:")
with open(filename, "r") as file:
    content = file.read()
    print(content)
with open(filename, "a") as file:
    file.write("This line was added later.\n")
print("Data appended successfully.\n")
print("Reading line by line:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())