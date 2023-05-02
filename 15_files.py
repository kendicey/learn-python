# open() & close()
file = open('15_text.txt', mode='r')
data = file.readline()
print(data)
file.close()

# with open auto-close the file
with open('15_text.txt', mode='r') as file:
    data = file.readline()
    print(data)

# create file -- with open()
with open('15_newfile.txt', 'w') as file:
    file.write("This is a new file created!")
    file.writelines(["\nSecond line", "\nThird line"])

# with open('15_newnewfile.txt', 'x') as file:
#     file.write("This is a new file created!")
#     file.writelines(["\nSecond line", "\nThird line"])

# append to file -- with open()
with open('15_newfile.txt', 'a') as file:
    file.writelines(["\nForth line", "\nFifth line"])

# with exception handling
try:
    with open('fake/fake.txt', 'a') as file:
        file.writelines(["\nForth line", "\nFifth line"])
except FileNotFoundError as e:
    print("ERROR", e)

# read(n) -- entire contents / number of characters in the file
with open('15_sample.txt', 'r') as file:
    # print(file.read())
    print(file.read(17))

# readline(n) -- return the first line / number of characters on a line
with open('15_sample.txt', 'r') as file:
    # print(file.readline())
    for x in file:
        print(x)

# readlines() -- return entire contents in an ordered list
with open('15_sample.txt', 'r') as file:
    print(file.readlines())
