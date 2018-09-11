filename = input('File path: ')

try:
    with open(filename,'r') as file:
        content = file.read()

    print(content)
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("No permission to read from the file.")

