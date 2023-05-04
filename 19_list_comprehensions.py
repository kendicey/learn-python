data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# List

# update the same list
data = [x+3 for x in data]
print("Updated list:", data)
# Updated list: [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]

# create a different list with updated values
new_data = [x*2 for x in data]
print("New list:", new_data)
# New list: [10, 12, 16, 20, 28, 32, 40, 44, 52, 64, 68]

# with if-condition
fourx = [x for x in new_data if x % 4 == 0]
print("Divisible by 4:", fourx)
# Divisible by 4: [12, 16, 20, 28, 32, 40, 44, 52, 64, 68]

# update list with if-condition
fourxsub = [x-1 for x in new_data if x % 4 == 0]
print("(Divisible by 4) - 1:", fourxsub)
# (Divisible by 4) - 1: [11, 15, 19, 27, 31, 39, 43, 51, 63, 67]

# with range()
tens = [x for x in range(100) if x % 10 == 0]
print("Tens:", tens)
# Tens: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
