# . Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(name, surname, year_of_birth, hometown, email, phone):
  #  print(f'имя - {name}, фамилия  - {surname}, год рождения - {year_of_birth}, город  - {hometown}, email - {email}, телефон - {phone}')
    for el in [name, surname, year_of_birth, hometown, email, phone]:
        print(f' {el}', end=' ')


user('Имя', 'Фамилия', 1990, 'Казань', 'аорарар', 911)
