def fibo_cycle(n):
    num_1 = 0
    num_2 = 1

    for _ in range(n-2):
        num = num_1 + num_2
        num_1 = num_2
        num_2 = num

    return num


def main():
    num_input = int(input('Input num for calculating string of fibonacci: '))
    print(fibo_cycle(num_input))


if __name__ == '__main__':
    main()
