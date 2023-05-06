import numpy as np

# zeros(n) create an array with n number of zeros
a = np.zeros(5)
print(a)         # [0. 0. 0. 0. 0.]

# full((a,b), c) create two-dimensional matrix of dimension a x b consisting the values c
b = np.full((2,3), 'X')
print(b)         # [['X' 'X' 'X']
                 # ['X' 'X' 'X']]

# linspance(a,b,c) divides the values between a and b in c equal parts
c = np.linspace(0,100,5)
print(c)         # [  0.  25.  50.  75. 100.]

print(type(c))   # <class 'numpy.ndarray'>

# ndarray is a substitute for lists in numpy which is more efficient