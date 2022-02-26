"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import timeit
array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    max_count = max(array, key=lambda i: array.count(i))
    return f'Чаще всего встречается число {max_count}, ' \
           f'оно появилось в массиве {array.count(max_count)} раз(а)'


print(func_1())
print(timeit.timeit(stmt="func_1", number=10000000, globals=globals()))
print(func_2())
print(timeit.timeit(stmt="func_2", number=10000000, globals=globals()))
print(func_3())
print(timeit.timeit(stmt="func_3", number=10000000, globals=globals()))
"""
в третьей функции для решения залачи применена функция max и lambda-функция
замеры времени в одном случае показывают лучшее быстродействие первой и второй функций, 
в другом - третьей функции"""