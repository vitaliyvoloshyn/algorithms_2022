"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import uuid
import hashlib


class CashClass:
    def __init__(self):
        self.dict = {}

    def create_hash(self, url):
        salt = uuid.uuid4().hex
        return hashlib.sha512(salt.encode() + url.encode()).hexdigest() + ':' + salt

    def add_to_cash(self, url):
        self.dict[url] = self.create_hash(url)

    def get_hash(self, url):
        if self.dict.get(url) is not None:
            return self.dict.get(url)
        else:
            self.add_to_cash(url)
            return None

    def all_cash(self):
        for key, val in self.dict.items():
            print(f"{key} - {val}")


a = CashClass()
print(a.get_hash('gb.ru'))
print(a.get_hash('google.com'))
print(a.get_hash('yandex.ru'))
print(a.get_hash('google.com'))
print(a.get_hash('wikipedia.org'))
a.all_cash()
