# basic function
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)


print(calculate_tax(175.00, 15))
print(calculate_tax(164.33, 22))


# global scope
my_global = 10


def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        print('Access to Global', my_global)
        print('Access to enclosed', enclosed_v)
    fn2()


fn1()
