"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


# Вариант 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


@profile
def my_func():
    d = factorial(4)
    return d


print(my_func())


# Вариант 2
@profile
def g(n):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    return factorial(n)


print(g(4))

# проблема заключается в том, что профилирование памяти происходит при каждом вызове рекурсивной функции
