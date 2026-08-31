#Program for writing in the file and read it
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Data written to '{filename}' successfully.")
    
def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(f"Contents of '{filename}':")
    print(content)
    
filename = "1.txt"
text_to_write = "Hello, this is a sample file.\nPython file handling is easy!"

write_to_file(filename, text_to_write)
read_from_file(filename)