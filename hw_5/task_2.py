def triangle_square_and_perimeter(a, b):  # returns 2 values
    c = (a**2 + b**2)**0.5
    square_triangle = a * b / 2
    perimeter_triangle = a + b + c

    return square_triangle, perimeter_triangle


if __name__=='__main__':
    side_a = int(input('Input length cathetics a: '))
    side_b = int(input('Input length cathetics b: '))

    square, perimeter = triangle_square_and_perimeter(side_a, side_b)

    print(f'Square of triangle = {square}\nPerimeter of triangle = {perimeter}')
