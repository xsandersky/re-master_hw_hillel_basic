
def index(lst, elem):  # returns integer or None
    for idx, element in enumerate(lst):
        if element == elem:
            return idx


def main():
    lst = [i for i in range(100, 111)]

    print(index(lst, 115))


if __name__ == '__main__':
    main()