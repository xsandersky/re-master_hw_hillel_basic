def my_sum(*digits, start=0):
    result = sum(digits) + start
    return result


print(my_sum(2, 2, 3, 5, 6, 7, start=22))
