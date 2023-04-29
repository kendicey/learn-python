# General
a = 10.0
print(type(a))

b = 2.3
print(type(b))

c = 'asfgvrwg'
print(type(c))

d = [1, 2, 3, 4]
print(type(d))

# String
name = 'John ' \
       'Doe'
print(name)
print(name[0])
print(len(name))

a = "my favorite food is "
b = "mashed potatoes"
print(a + b)

# Input
print("Where do you live?")
location = input()
print("So you live in " + location)

print(float(10))

you = 'Mann'


def say_hello(you):
    return "Hello " + you


print(say_hello(you))

print('Hello', 'you!', sep=', ')

print("I like {0} more than {1}".format("oranges", "grapes"))
