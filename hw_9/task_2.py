from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound) -> int: # returns int
    lst = [randint(lower_bound, upper_bound + 1) for _ in range(num_limit)]
    sum_divide_2 = 0
    sum_not_divide_2 = 0

    for i in lst:
        if i % 2 == 0:
            sum_divide_2 += i
        else:
            sum_not_divide_2 += i

    return sum_divide_2 - sum_not_divide_2


def main():
    n = int(input(f'Input the amount of digits: '))
    lower_digit = int(input(f'Enter lower digit: '))
    upper_digit = int(input(f'Enter upper digit: '))

    print(diff_min_max(n, lower_digit, upper_digit))


if __name__ == '__main__':
    main()
