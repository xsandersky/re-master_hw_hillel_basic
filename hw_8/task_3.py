def main():
    lst = [5, '9', 0, '452', 6.5, '6', 1, 2]
    print(sorted(lst, key=float))

    lst = [472, 326, 1, 999.0, '1101000', '99', 9, '20', 863, '0']
    print(sorted(lst, key=lambda x: str(x)[0]))


if __name__ == '__main__':
    main()
