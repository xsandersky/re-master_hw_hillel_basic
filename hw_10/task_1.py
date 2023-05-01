def copydeep(object, memory=None):
    if memory is None:
        memory = {}

    if id(object) not in memory:
        if isinstance(object, list):
            new_object = []
            memory[id(object)] = new_object
            for elem in object:
                new_object.append(copydeep(elem, memory))
            return new_object

        elif isinstance(object, dict):
            new_object = {}
            memory[id(object)] = new_object
            for key, val in object.items():
                new_object[copydeep(key, memory)] = copydeep(val, memory)
            return new_object

        else:
            return object

    else:
        return memory[id(object)]


def main():
    test_data = [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658]}, 2.0, {'e': 0}]
    test_data[3]['d'] = test_data
    test_data[-1]['f'] = test_data[-1]
    copy = copydeep(test_data)
    print(test_data)
    # [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
    print(copy)
    # [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
    print(copy[3]['c'] is not test_data[3]['c'])  # True
    print(copy[3]['d'] is not test_data[3]['d'])  # True
    print(copy[3]['d'] is copy)  # True
    print(copy[-1] is not test_data[-1])  # True
    print(copy[-1] is copy[-1]['f'])  # True


if __name__ == "__main__":
    main()
