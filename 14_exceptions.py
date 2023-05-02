# general flow
def divide_by(a, b):
    return a / b


try:
    ans = print(divide_by(40, 0))
except Exception as e:
    print("Something went wrong!", e)
    print(e.__class__)


try:
    ans = print(divide_by(sdg, 0))
except ZeroDivisionError as e:
    print(e, "! We cannot divide by zero")
except Exception as e:
    print(e, "! Something went wrong!")

# IndexError
items = [1, 2, 3, 4, 5]

try:
    item = items[6]
    print(item)
except IndexError as e:
    print(e, "! Item does not exist in the list")

# FileNotFoundError
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e, "! The file could not be found")
