#Для списка реализовать обмен значений соседних элементов.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#При нечётном количестве элементов последний сохранить на своём месте.
#Для заполнения списка элементов нужно использовать функцию input().

a=list(input('Введите элементы списка - '))
s=[]
for el in a:
    var_1, var_2 = a.pop(0), a.pop(0)
    # if var_2 == None:
    #     s.append(var_1)
    var_1, var_2 = var_2, var_1
    s.append(var_1)
    s.append(var_2)
print(s)
 #Почему не работает для последних трех элементов????????????????????????


# ваши решения
# my_list = list(input('Введите числа без пробелов - '))
# for i in range(1, len(my_list), 2):
#     my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
# print(my_list)


# user_list = input('Введите числа с пробелами - ').split( )
# for i in range(1, len(user_list), 2):
#     user_list.insert(i-1, user_list.pop(i))
# print(user_list)

