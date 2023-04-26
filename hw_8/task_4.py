def gen_primes():  # returns list of ints
    new_lst = [2]

    for num in range(3, 101):
        calc = 0
        for i in range(2, num):
            if num % i == 0:
                calc += 1
        if calc == 0:
            new_lst.append(num)

    return new_lst




def main():
    x = gen_primes()
    print(x)


if __name__ == '__main__':
    main()
