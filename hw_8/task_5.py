from random import  randint


def get_max_digit(number):  # returns int
    number = list(str(number))
    return int(max(number))


def main():
    x = randint(10**12, 10**13 - 1)
    print(get_max_digit(x))


if __name__ == '__main__':
    main()
