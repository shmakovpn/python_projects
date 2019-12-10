#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 59
Подсчет ссыллок и сборка мусора
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"
import sys
import copy

d = []
for x in range(10):
    d.append("123")
z = "123"
print(f"z ref count={sys.getrefcount(z)}")  # prints 14
a = z
print(f"a ref count={sys.getrefcount(a)}")  # prints 15

x1 = 13
x2 = 13
print(f"x1 ref count={sys.getrefcount(x1)}")  # prints 16

x3 = 13
print(f"x1 ref count={sys.getrefcount(x1)}")  # prints 16

print(f"34532 ref count={sys.getrefcount(34532)}")  # prints 3
print(f"ref count={sys.getrefcount(345687)}")  # prints 3

# стр 60 ссылки и копии
a = [1, 2, 3, 4]
b = a
print(f"b is a = {b is a}")
b[2] = -100
print(f"a = {a}")  # a тоже поменялось

# поверхностное копирование
# При поверхностном копировании создается новый объект, но он
# будет заполнен ссылками на элементы, которые содержались в оригинале.
a = [1, 2, [3, 4]]
b = list(a)  # Создание поверхностной копии списка a
print(f"b is a = {b is a}")
b.append(100)
print(f"b={b}")
print(f"a={a}")
b[2][0] = -100
print(f"b={b}")
print(f"a={a}")
# глубокое копирование
# При глубоком копировании создается новый объект и рекурсивно создаются копии всех объектов, содержащихся в оригинале.
c = copy.deepcopy(a)
c[2][0] = 345
print(f"a={a}")
print(f"c={c}")
