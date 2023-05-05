# import math as m      # you can also assign alias to the imported module
from math import sqrt as SQRT  # import specific module to avoid overloading, can use alias to functions also

# root = m.sqrt(9)  # use alias to access functions
root = SQRT(9)  # need not to specific the math module

print(root) # 3.0


# # import multiple modules at once
# from math import factorial, log10, sqrt

# x = log10(50)
# print(x)
