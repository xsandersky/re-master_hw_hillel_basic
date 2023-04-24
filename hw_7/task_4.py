def sum_unicode_char(start, end):
    num_from_start = ord(start)
    num_from_end = ord(end)

    sum_unicode = 0
    for i in range(num_from_start, num_from_end + 1):
        sum_unicode += i

    return sum_unicode


def main():
    char_1, char_2 = input('Input first char: ').lower(), input('Input second char: ').lower()

    print(f'Sum of all unicode char between {char_1} and {char_2} = {sum_unicode_char(char_1, char_2)}')


if __name__ == '__main__':
    main()
