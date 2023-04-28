def group_by_surname(list_of_enrollees): # returns 4 ints
    group = {
        'A-I':0,
        'J-P':0,
        'Q-T':0,
        'U-Z':0
        }

    for elem in list_of_enrollees:
        elem = elem.split()
        if ord('A') <= ord(elem[1][0]) < ord('J'):
            group['A-I'] += 1
        elif ord('J') <= ord(elem[1][0]) < ord('Q'):
            group['J-P'] += 1
        elif ord('Q') <= ord(elem[1][0]) < ord('U'):
            group['Q-T'] += 1
        else:
            group['U-Z'] += 1

    return [val for val in group.values()]


def test():
    count_students = group_by_surname(['Will Smith', 'Emma Watson', 'George Clooney', 'Jay Z', 'David Beckham'])
    assert count_students == [2, 0, 1, 2]


def main():
    test()
    lst_names = ['George Clooney', 'Will Smith', 'Emma Watson', 'Jay Z', 'David Beckham']
    count_students = group_by_surname(lst_names)

    print(f'In group \'A-I\' - {count_students[0]} student')
    print(f'In group \'J-P\' - {count_students[1]} student')
    print(f'In group \'Q-T\' - {count_students[2]} student')
    print(f'In group \'U-Z\' - {count_students[3]} student')


if __name__ == '__main__':
    main()
