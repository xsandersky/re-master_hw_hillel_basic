def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def test():
    assert sign(2) == 1
    assert sign(0) == 0
    assert sign(-222) == -1


def main():
    user_input = float(input('Input some number: '))
    print(sign(user_input))


if __name__ == '__main__':
    main()
