def walk_horse(cell_1, cell_2):
    x1, y1 = list(cell_1)
    x2, y2 = list(cell_2)

    dif_x = abs(ord(x2) - ord(x1))
    dif_y = abs(int(y2) - int(y1))

    if dif_x == 1 and dif_y ==2 or dif_x == 2 and dif_y == 1:
        return True
    else:
        return False


def main():
    user_input_1 = input('Input cell_1: ')
    user_input_2 = input('Input cell_2: ')

    print(walk_horse(user_input_1, user_input_2))


if __name__ == '__main__':
    main()