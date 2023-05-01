list1 = [1, 2, 3, 4, 5]

print(list1[0])                 # 1
print(*list1)                   # 1 2 3 4 5
print(list1, sep=" ")           # [1, 2, 3, 4, 5]

list1.insert(len(list1), 6)
print(*list1)                   # 1 2 3 4 5 6

list1.append(7)
print(*list1)                   # 1 2 3 4 5 6 7

list1.extend([8, 9, 10, 11])
print(*list1)                   # 1 2 3 4 5 6 7 8 9 10 11

list1.pop(4)                    # remove index[4] element
print(*list1)                   # 1 2 3 4 6 7 8 9 10 11

del list1[2]                    # remove index[2] element
print(*list1)                   # 1 2 4 6 7 8 9 10 11

for x in list1:                 # iterate though the list
    print(x)

list2 = ['A', 'B', 'C']
list3 = ['Hello', 1, True, 40.22]
list4 = [1, [2, 3, 4], 5, 6]
