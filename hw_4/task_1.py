# Написати програму, що перетворює значення рядкової змінної з формату snake_case в формат CapitalizedWords
# (a.k.a. Capitalized camelCase). Значення змінної отримуйте з input(). Для простоти вважаємо,
# що значення змінної завжди складається з 3-х слів, але, можна оброблювати і "загальний випадок",
# тобто, коли будь-яка кількість слів. Наприклад: 'employee_first_name' -> 'EmployeeFirstName'.
text = input('Input some text: ')
lst = text.split('_')

lst = [i.capitalize() for i in lst]
final_str = ''.join(lst)

print(final_str)

#_____________________________________________
txt = input('Input some text: ').title()
txt = txt.replace('_', '')

print(txt)

