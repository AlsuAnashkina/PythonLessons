# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.Строки необходимо пронумеровать.Если в слово длинное, выводить
# только первые 10 букв в слове.

str_1 = input('Введите строку из нескольких слов - ')
a = str_1.split( )
for ind, el in enumerate(a, 1):
    print(ind, el[0:10])