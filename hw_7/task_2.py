def my_func(start, end):
    lst = []

    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append('FizzBuzz')
        elif i % 5 == 0:
            lst.append('Buzz')
        elif i % 3 == 0:
            lst.append('Fizz')
        else:
            lst.append(i)

    return '\n'.join(map(str, lst))


def main():
    start = int(input('INput start value: '))
    end = int(input('INput end value: '))

    print(my_func(start, end))


if __name__ == '__main__':
    main()
