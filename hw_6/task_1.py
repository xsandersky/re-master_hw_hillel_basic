def is_even(number): # returns boolean value
    return True if number % 2 == 0 else False


def main():
    input_number = int(input('Input smt number: '))
    print(is_even(input_number))


if __name__=='__main__':
    main()
