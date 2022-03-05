"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {i: i ** 2 for i in range(100000)}
ord_dict = OrderedDict(my_dict)


def dict_popitem(n):
    for i in range(n):
        return my_dict.popitem()


def ord_dict_popitem(n):
    for i in range(n):
        return ord_dict.popitem()


def dict_get(n):
    for i in range(n):
        return my_dict.get(i)


def ord_dict_get(n):
    for i in range(n):
        return ord_dict.get(i)


print(f'dict - операция popitem - {timeit(stmt="dict_popitem(n)", setup="n = 10000", number=1, globals=globals())}')
print(f'OrderedDict - операция popitem - \
{timeit(stmt="ord_dict_popitem(n)", setup="n = 10000", number=1, globals=globals())}')
print(f'dict - операция get - {timeit(stmt="dict_get(n)", setup="n = 10000", number=1000, globals=globals())}')
print(
    f'OrderedDict - операция get - {timeit(stmt="ord_dict_get(n)", setup="n = 10000", number=1000, globals=globals())}')
# dict - операция popitem - 4.7400000000002995e-05
# OrderedDict - операция popitem - 9.100000000011876e-06
# dict - операция get - 0.0010346999999999995
# OrderedDict - операция get - 0.0011753999999999931
# операция popitem в ordereddict выполняется быстрее, чем у обычного словаря
# операция get в ordereddict и у обычного словаря выполняется с одинаковой скоростью
