my_d = {1: 'Test', 'Name': 'Jim'}

print(my_d)                 # {1: 'Test', 'Name': 'Jim'}
print(my_d[1])              # Test

my_d[2] = 'Test 2'
print(my_d)                 # {1: 'Test', 'Name': 'Jim', 2: 'Test 2'}

my_d[1] = 'Not a test!'
print(my_d)                 # {1: 'Not a test!', 'Name': 'Jim', 2: 'Test 2'}

del my_d[1]
print(my_d)                 # {'Name': 'Jim', 2: 'Test 2'}

for x in my_d:              # iterate through keys only
    print(x)                # Name 2

for key, value in my_d.items():
    print(str(key) + " : " + value)     # Name : Jim
    # 2 : Test 2
