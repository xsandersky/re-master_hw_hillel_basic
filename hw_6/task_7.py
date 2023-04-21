def fibo(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)


def main():
    print(f'10 digit in Fibonacci = {fibo(10)}')


if __name__ == '__main__':
    main()
