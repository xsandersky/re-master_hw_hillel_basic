num = int(input('Input random numeric: '))
final = ''

b,c  = divmod(num, 2)
final += str(c)
b,c  = divmod(b, 2)
final += str(c)
b,c  = divmod(b, 2)
final += str(c)
b,c  = divmod(b, 2)
final += str(c)
b,c  = divmod(b, 2)
final += str(c)
b,c  = divmod(b, 2)
final += str(c)

bool_num = int(final[::-1])

print(f'Number {num} in bool = {bool_num}')
