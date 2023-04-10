from math import sqrt

a = 1
b = 5
c = 4

x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

print(f'x1 = {x1}\nx2 = {x2}')
