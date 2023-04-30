for i in range(10):
    print("Looping ...", i)


colors = ['red', 'blue', 'green', 'yellow']

for index, color in enumerate(colors):
    print(index, "-", color)

count = 0

while count < len(colors):
    print('I like', colors[count])
    count += 1


for i in range(2):
    for j in range(10):
        print(0, end=" ")
    print()
