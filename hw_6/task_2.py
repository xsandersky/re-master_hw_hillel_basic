def solve_quadratic_equation(a, b, c):
    discr = b**2 - 4*a*c

    if discr > 0:
        return (-b + discr**0.5) / (2*a), (-b - discr**0.5) / (2*a)
    elif discr == 0:
        return -b / (a * 2), None
    else:
        return None, None


def main():
    a, b, c = float(input('Input a: ')), float(input('Input b: ')), float(input('Input c: '))
    x1, x2 = solve_quadratic_equation(a, b, c)

    if x1 is None and x2 is None:
        print('There are no roots.')
    elif x1 is None or x2 is None:
        if x1 is None:
            print(f'Quadratic equation has 1 root x = {x2}')
        else:
            print(f'Quadratic equation has 1 root x = {x1}')
    else:
        print(f'Quadratic equation has 2 roots:\nx1 = {x1},\nx2 = {x2}')


def test():
    assert solve_quadratic_equation(1, -4, 3) == (3, 1)
    assert solve_quadratic_equation(1, -6, 9) == (3, None)
    assert solve_quadratic_equation(1, 2, 5) == (None, None)


if __name__=='__main__':
    test()
    main()
