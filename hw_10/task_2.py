# Створити функцію "генератор паролів", що повертає згенеровані паролі сумісні з наступними вимогами.
# Можна використовувати лише криптостійкі функції для генерації паролю.
# Вимоги:
# Пароль складається мінімум з 8 символів, потрібну довжину приймати параметром, але не менше 8
# В паролі допускаються лише великі та маленькі латинські літери, цифри та символ підкреслення "_".
# Використайте змінні з модулю string (UKR)
# Пароль обов'язково має містити щонайменше одну велику літеру, одну маленьку літеру та одну цифру
# Не повинно бути більше 2 однакових символів підряд

import secrets
import string


def get_input(promt):
    while True:
        try:
            user_input = int(input(promt))
        except:
            print('The program only accepts numbers as input: ')
            continue
        else:
            if user_input > 7:
                break
            print('Input number more than 7: ')

    return user_input


def gen_pass(n):
    data_for_pass = string.ascii_letters + string.digits + '_'
    new_pas = {}

    while True:
        while len(new_pas)!= n:
            random_char = secrets.choice(data_for_pass)
            new_pas[random_char] = random_char

        if any(c.islower() for c in new_pas) and\
                any(c.isupper() for c in new_pas) and\
                any(c.isdigit() for c in new_pas):
            break

    return ''.join(new_pas.keys())


def main():
    count_of_char = get_input('Input from amount characters would create password: ')
    print(gen_pass(count_of_char))


if __name__ == '__main__':
    main()
