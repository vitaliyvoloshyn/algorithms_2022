"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def my_func():
    def suma(n, num=1, i=1, cur_sum=1):
        if i == n:
            return i, cur_sum
        i += 1
        num /= -2
        cur_sum += num
        return suma(n, num, i, cur_sum)

    try:
        user_num = int(input('Введите количество элементов: '))
        i, y = suma(user_num)
        print(f"Количество элементов - {i}, их сумма - {y}")
    except ValueError:
        print('Вы ввели строку')
        return my_func()


my_func()
