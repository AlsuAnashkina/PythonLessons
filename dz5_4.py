# Создать (не программно) текстовый файл со следующим содержимым:One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}

with open('dz5_4.txt', 'r', encoding='utf-8') as df, open('newdz5_4.txt', 'w', encoding='utf-8') as new:

    for line in df:
        new_list = []
        a = (line.lower()).split( )
        a.insert(0, my_dict.get(a.pop(0)))
        for el in a:
            new_list.append(el)
        new.write((' '.join(new_list)).capitalize())

# Куда воткнуть перевод строки?
