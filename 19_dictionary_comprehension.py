# Using range() function and no input list
# {x: x*2}, while x iterates from 0 to 12
usingRange = {x: x*2 for x in range(6)}
print("Using range():", usingRange)
# Using range(): {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
          "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using one input list
numDict = {x: x**2 for x in number}
print("Using one input list to create Dict:", numDict)
# Using one input list to create Dict: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

# Using two input lists
monthsDict = {key: value for (key, value) in zip(number, months)}
print("Using two lists:", monthsDict)
# Using two lists: {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
