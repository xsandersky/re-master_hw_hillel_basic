# Даний рядок вигляду 'Taras Shevchenko*1814-03-09*1861-03-10',
# тобто вказане ім'я, прізвище та дати народження та смерті. Написати програму, що отримуючи такий рядок через input()
# виводить на екран окремими рядками ім'я та прізвище людини та її вік в роках.Для простоти при розрахунку віку можете
# ігнорувати число місяця та місяць. Тобто для рядку 'Taras Shevchenko*1814-03-09*1861-03-10' програма має вивести:
#
# Name: Taras Schevchenko
# Age: 47 years

user_input = input('Input something text: ')

list_user_input = user_input.split('*')
list_born_year = list_user_input[1].split('-')
list_death_year = list_user_input[2].split('-')
age = int(list_death_year[0]) - int(list_born_year[0])

print(f'Name: {list_user_input[0]}\nAge: {age} years')
#--------------------------------------------------------------------------
