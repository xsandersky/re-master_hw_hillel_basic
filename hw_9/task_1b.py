from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound) -> int: # returns int
    lst = [randint(lower_bound, upper_bound + 1) for i in range(num_limit)]
    lst.sort()

    return lst[-1] - lst[0]


def main():
    n = int(input(f'Input the amount of digits: '))
    lower_digit = int(input(f'Enter lower digit: '))
    upper_digit = int(input(f'Enter upper digit: '))

    print(diff_min_max(n, lower_digit, upper_digit))


if __name__ == '__main__':
    main()
