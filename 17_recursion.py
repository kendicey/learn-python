# non-recursion
def find_factorial(n):
    ans = 1
    for x in range(n):
        ans *= (x + 1)
    return ans

# recursion


def find_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n-1)


print(str(5*4*3*2*1))               # 120
print(find_factorial(5))            # 120
print(find_factorial_recursive(5))  # 120
