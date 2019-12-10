#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 46
Модули
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"


import div
a, b = div.divide(2305, 29)
print(f"a={a}, b={b}")

import div as foo
c, d = foo.divide(2305, 29)
print(f"c={c}, d={d}")

from div import divide
x, y = divide(2305, 29)
print(f"x={x}, y={y}")

import string
print(f"{dir(string)}")

# получение справки
print(f"{issubclass.__doc__}")


# комплексные числа
print(f"complex result={(3 + 4j)*(5 - 2j)}")
print(f"real={(5+3j).real}")
print(f"real={(5+3j).imag}")
print(f"type={type(6+7j)}")
print(f"type={type(6.4+7.64j)}")
print(f"type={type(6)}")
print(f"type={type(6.556)}")

# использование экранирования символов (стр 52)
print(f"Jalape\xf1o")


# строки документирования
def fact(n):
    """
    Эта функция находит факториал числа
    :param n: аргумент
    :return: факториал от аргумента
    """
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


print(f"{fact.__doc__}")
print(f"{help(fact)}")
