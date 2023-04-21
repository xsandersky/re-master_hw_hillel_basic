def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
    distance_between_center = (x1 - x2)**2 + (y1 - y2)**2

    if (r2 - r1)**2 <= distance_between_center <= (r1 + r2)**2:
        return True
    else:
        return False


def main():
    x1, y1, r1 = float(input('Input x1 coordinate: ')), float(input('Input y1 coordinate: ')), float(input('Input r1 coordinate: '))
    x2, y2, r2 = float(input('Input x2 coordinate: ')), float(input('Input y2 coordinate: ')), float(input('Input r2 coordinate: '))

    print(circles_intersect(x1, y1, r1, x2, y2, r2))


if __name__ == '__main__':
    main()
