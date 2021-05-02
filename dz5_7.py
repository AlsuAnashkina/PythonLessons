# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее
# еализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
finacial_result = []
profits = {}

with open('dz5_7.txt', 'r', encoding='utf-8') as dz:
    counter = 0
    average_profit = 0
    for line in dz:
        a = line.split( )
        profit = int(a[2]) - int(a[3])
        new_dict = {a[0]:profit}
        profits.update(new_dict)
        if profit >= 0:
            average_profit += profit
            counter +=1
    avpr = average_profit / counter
    av_pr = {'average_profit':avpr}

finacial_result.append(profits)
finacial_result.append(av_pr)
print(finacial_result)