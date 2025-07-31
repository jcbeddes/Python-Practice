file_path = "C:/Users/jcbed/Desktop/testing.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")