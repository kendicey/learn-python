import os

# # os.listdir() list all files inside the directory
# contents = os.listdir(r'C:\Users\kendi\Desktop\GitHub\learn-python\22_modules_reload')
# print(contents)     # ['filechanges.py', 'reloads.py', 'sample.py', '__pycache__']


def print_changes():
    contents = os.listdir(r'C:\Users\kendi\Desktop\GitHub\learn-python\22_modules_reload')
    print("Current directory contents:")
    print(contents)