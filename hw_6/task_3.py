def solve_quadratic_equation(a, b, c):
    discr = complex(b)**2 - 4*complex(a)*complex(c)
    return (-b + discr**0.5) / (2*a), (-b - discr**0.5) / (2*a)


def main():
    a, b, c = float(input('Input a: ')), float(input('Input b: ')), float(input('Input c: '))
    x1, x2 = solve_quadratic_equation(a, b, c)

    print(f'Quadratic equation has 2 roots:\nx1 = {x1},\nx2 = {x2}')


if __name__=='__main__':
    main()
