my_tuple = (1, 'abc', 4.5, True)

print(my_tuple[0])              # 1
print(type(my_tuple[0]))        # <class 'int'>
print(my_tuple.count('abc'))    # 1
print(my_tuple.index(4.5))      # 2

my_tuple[0] = 100               # error (immutable)

for x in my_tuple:
    print(x)
