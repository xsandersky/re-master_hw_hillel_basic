from math import pi
def cone_square_and_volume(radius, height):  # returns 2 floats
    sq = pi * radius**2 + pi * radius * (radius**2 + height**2)**0.5
    vol = pi * radius**2 * height / 3

    return sq, vol


if __name__=="__main__":
    get_radius = int(input('Input radius: '))
    get_height = int(input('Input height: '))

    square, volume = cone_square_and_volume(get_radius, get_height)

    print(f'Square of cone = {square}\nVolume = {volume}')
  