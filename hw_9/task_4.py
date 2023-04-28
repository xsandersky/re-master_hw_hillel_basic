def lchain(*iterables):  # returns list
    lst = []

    for elem in iterables:
        if elem is list:
            lst.extend(elem)
        else:
            lst.extend(list(elem))

    return lst


def test():
    print('Запуск теста')
    assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]
    print('Выход из теста')


def main():
    a = [1, 2, 3]
    b = tuple()
    c = (4, 5)
    d = {'6': 6, 7:'7'}
    e = range(10, 20)

    print(lchain(a, b, c, d, e))


if __name__ == '__main__':
    main()
