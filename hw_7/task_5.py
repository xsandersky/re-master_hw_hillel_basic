from random import randint

def main():
    num_from_pc = randint(1, 10)
    user_input = int(input('Input num from 1 to 10: '))

    while num_from_pc != user_input:
        user_input = int(input('Input another num: '))


if __name__ == '__main__':
    main()
