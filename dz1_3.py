# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

a=int(input('Введите число от 1 до 9-'))
summa=a+a*11+a*111
print(f'Сумма чисел {a}+{a}{a}+{a}{a}{a} равна -', summa)

# b=input('Введите число от 1 до 9-')
# print(f'{b} + {b+b} + {b+b+b} = {int(b) + int(b+b) + int(b + b + b)}')



