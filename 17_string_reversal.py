# extended slice method
# str[start:stop:step]

trial = "reversal"
# start & stop indexes are omitted to included all elements
# step value of 1 means that the slice will include every element 1-by-1
# step value of -1 means that the slice will include every element 1-by-1 starting from the -1 index (last element)
new_trial = trial[::-1]
print(new_trial)


# recursion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        # exclude first character (from index 1 to the end)
        # string_reverse("BCD")
        # string_reverse("CD")
        # string_reverse("D")
        # string_reverse("") -> len(str) == 0 -> return ""
        # + 'D'
        # + 'C'
        # + 'B'
        # + 'A'
        return string_reverse(str[1:]) + str[0]


str = "ABCD"
reverse = string_reverse(str)
print(reverse)
