def copydeep(object):
    if isinstance(object, (list, tuple)):
        new_obj = [copydeep(i) for i in object]
        return type(object)(new_obj)

    elif isinstance(object, dict):
        new_obj = {copydeep(key): copydeep(val) for key, val in object.items()}
        return new_obj

    else:
        return object


def main():
    obj_1 = {'a': "a", "1": 1, "2": 2.0, 3: "b"}
    obj_2 = copydeep(obj_1)
    obj_1[3] = "c"

    print(obj_1)
    print(obj_2)
    print(obj_1[3], obj_2[3])


if __name__ == "__main__":
    main()