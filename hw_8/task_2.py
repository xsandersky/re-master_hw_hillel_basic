def copydeep(object):
    obj_type = type(object)
    new_obj = []

    for elem in object:
        if isinstance(elem, (list, tuple)):
            elem_type = type(elem)
            new_elem = elem_type(elem[:])
            new_obj.append(copydeep(new_elem))
        else:
            new_obj.append(elem)

    return obj_type(new_obj)


def main():
    lst1 = ['a', 1, 2.0, ['b']]

    lst2 = copydeep(lst1)
    lst1[3].append(0)

    print(lst1[3], lst2[3])


if __name__ == '__main__':
    main()
