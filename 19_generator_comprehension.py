data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

gen_obj = (x for x in data)
print(gen_obj)  # <generator object <genexpr> at 0x000001BB2C3492F0>
print(type(gen_obj))    # <class 'generator'>
for items in gen_obj:
    print(items, end=" ")   # 2 3 5 7 11 13 17 19 23 29 31
