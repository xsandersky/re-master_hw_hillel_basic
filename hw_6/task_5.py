def high_year(number):
    return 'Yes' if (number % 4 == 0 or number % 400 == 0) and number % 100 != 0 else 'No'


def test():
    assert high_year(100) == 'No'
    assert high_year(33) == 'No'
    assert high_year(400) == 'No'
    assert high_year(4) == 'Yes'
    assert high_year(404) == 'Yes'


def main():
    input_from_user = int(input('Input some number whist you want to check: '))

    print(high_year(input_from_user))


if __name__ == '__main__':
    main()
