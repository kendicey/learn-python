import random

# f = open("15_petnames.txt", "r")
f_name = input("Type the file name: ")
f = open(f_name)  # default mode is 'r'
f_content = f.read()
# print(f_content)
f_content_list = f_content.split("\n")
# print(f_content_list)
print(random.choice(f_content_list))
