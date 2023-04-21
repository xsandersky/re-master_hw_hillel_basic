from math import log2


def cell_from_weght(grain_kg):
    grain = log2(grain_kg / 0.000035)
    cells = 'abcdefgh'

    return cells[int(grain)//8] + str(int(grain) % 8 + 1)


def main():
    user_input = float(input('Input quantity kg grain: '))

    print(cell_from_weght(user_input))


if __name__ == '__main__':
    main()
