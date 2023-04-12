# a) З використанням рядків (тобто після input заборонено приводити введене число до int/float/Decimal безпосередньо).
get_num = input('Input some 3-digit number: ')

sum_all_digits = int(get_num[0]) + int(get_num[1]) + int(get_num[2])


print(sum_all_digits)

# b) Без використання обробки рядків
get_some_num = int(input('Input somr three digit number: '))

digits_sum = get_some_num % 10 + get_some_num // 10 % 10 + get_some_num // 100

print(digits_sum)