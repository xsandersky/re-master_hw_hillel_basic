from math import pi
def degrees2radians(degrees):
    radians = degrees * (pi / 180)
    return radians

if __name__=='__main__':
    print(f'Degree 60 = {degrees2radians(60)}\nDegree 45 = {degrees2radians(45)}\nDegree 40 = {degrees2radians(40)}')
