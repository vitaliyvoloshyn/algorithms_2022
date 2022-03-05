"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple as nt

lst_obj = []  # список для хранения обьектов namedtuple
lst_down = []  # список для сохранения компаний с прибылью ниже среднего
lst_up = []  # список для сохранения компаний с прибылью выше среднего
obj = nt('company', 'name kv1 kv2 kv3 kv4')
for i in range(int(input('Введите количество предприятий для расчета прибыли: '))):
    name = input('Введите название предприятия: ')
    kv_list = list(map(int, input('через пробел введите прибыль данного предприятия \
за каждый квартал(Всего 4 квартала): ').split()))
    obj_1 = obj(name=name, kv1=kv_list[0], kv2=kv_list[1], kv3=kv_list[2], kv4=kv_list[3])
    lst_obj.append(obj_1)
# просчет средней годовой прибыли всех предприятий:
average_profit = 0
for n in lst_obj:
    average_profit += n.kv1 + n.kv2 + n.kv3 + n.kv4
average_profit /= len(lst_obj)
for n in lst_obj:
    if (n.kv1 + n.kv2 + n.kv3 + n.kv4) > average_profit:
        lst_up.append(n.name)
    elif (n.kv1 + n.kv2 + n.kv3 + n.kv4) < average_profit:
        lst_down.append(n.name)
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {lst_up}')
print(f'Предприятия, с прибылью ниже среднего значения: {lst_down}')
