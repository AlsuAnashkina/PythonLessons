# . Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
with open('dz5_5.txt', 'w', encoding='utf-8') as dz:
    for el in range(10):
        print(randint(0, 50), file=dz, end=' ')

with open('dz5_5.txt', 'r', encoding='utf-8') as summ:
    content = (summ.read()).split( )
    content = [int(el) for el in content]
    print(f'Сумма чисел {content} равна - {sum(content)}')


