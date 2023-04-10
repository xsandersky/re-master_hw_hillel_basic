from math import cos

get_num = float(input('Input random numeric: '))
calc_tg = (1 - cos(get_num)**2)**0.5 / cos(get_num)
print(f'Tangent {get_num} = {calc_tg}')