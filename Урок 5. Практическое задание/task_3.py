"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

dq = deque()
lst = []
lst1 = [i for i in range(100)]
dq1 = deque(lst1)

def dq_app(n, ):
    for i in range(n):
        dq.append(i)


def lst_app(n):
    for i in range(n):
        lst.append(i)


def dq_pop(n):
    for i in range(n):
        dq.pop()


def lst_pop(n):
    for i in range(n):
        lst.pop()


def dq_ext():
    dq.extend(dq1)


def lst_ext():
    lst.extend(lst1)


def app_left(n):
    for i in range(n):
        dq.appendleft(i)


def lst_ins(n):
    for i in range(n):
        lst.insert(0, i)


def pop_left(n):
    for i in range(n):
        dq.popleft()


def lst_pop0(n):
    for i in range(n):
        lst.pop(0)




def get_dq(n):
    for i in range(n):
        return dq1[i]


def get_lst(n):
    for i in range(n):
        return lst1[i]


print(f'Добавление в дека - {timeit(stmt="dq_app(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Добавление в список - {timeit(stmt="lst_app(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Расширение дека - {timeit(stmt="dq_ext()", number=100, globals=globals())}')
print(f'Расширение списка - {timeit(stmt="lst_ext()", number=100, globals=globals())}')
print(f'Удаление из дека - {timeit(stmt="dq_pop(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Удаление из списка - {timeit(stmt="lst_pop(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Добавление в начало дека - {timeit(stmt="app_left(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Добавление в начало списка - {timeit(stmt="lst_ins(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Удаление из начала дека - {timeit(stmt="pop_left(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Удаление из начала списка - {timeit(stmt="lst_pop0(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Взятие по индексу из дека - {timeit(stmt="get_dq(n)", setup="n = 100", number=1000, globals=globals())}')
print(f'Взятие по индексу из  списка - {timeit(stmt="get_lst(n)", setup="n = 100", number=1000, globals=globals())}')

# Добавление в дека - 0.020020300000000005
# Добавление в список - 0.01668420000000001
# Расширение дека - 0.0001910999999999996
# Расширение списка - 8.319999999997774e-05
# Удаление из дека - 0.014522299999999988
# Удаление из списка - 0.014413700000000002
# Добавление в начало дека - 0.015562500000000007
# Добавление в начало списка - 7.5188786
# Удаление из начала дека - 0.014105500000000326
# Удаление из начала списка - 1.5516581999999994
# Взятие по индексу из дека - 0.0007790999999990333
# Взятие по индексу из  списка - 0.0008317999999984949

# как видно из замеров операция extend у списков проходит быстрее, чем у deque
# в то же время списки проигрываю перед deque в таких операциях как добавление в начало и удаление с начала