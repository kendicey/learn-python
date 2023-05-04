# print x from 10 to 19
# skip 12, 14. 16
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(set_a)
# {10, 11, 13, 15, 17, 18, 19}

# set_b is {40, 80, 20, 60} as set is unordered collections
set_b = {x for x in range(1, 100) if x % 20 == 0}
list_b = list(set_b)  # cast to list and sort()
list_b.sort()
print(list_b)
