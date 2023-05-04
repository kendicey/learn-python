menu = ['espresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']


def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee


map_coffee = map(find_coffee, menu)
print(map_coffee)   # map() returns an object <map object at 0x0000021FE2B97F40>
for x in map_coffee:
    print(x)

filter_coffee = filter(find_coffee, menu)
# filter() returns an object <filter object at 0x000001FC7F847EE0>
print(filter_coffee)
for x in filter_coffee:
    print(x)
