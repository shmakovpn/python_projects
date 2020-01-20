#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 172
Управление памятью объектов (как работают __new__ и __init__)
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-16"


class Circle(object):
    def __init__(self, radius):
        self.radius = radius


# Создать несколько экземпляров класса Circle
c = Circle(4.0)
# или тоже самое
cc = Circle.__new__(Circle, 4.0)
if isinstance(c, Circle):
    Circle.__init__(c, 4.0)


# попробуем переопределить метод __new__
class NewInit:
    def __new__(cls, *args, **kwargs):
        print(f"hello from NewInit.__new__")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print(f"hello from NewInit.__init__")


ni = NewInit()
print(f"ni={ni}")  # без return при вызове super().__new__ будет None, и __init__ не будет вызван


class Upperstr(str):
    def __new__(cls, value=""):
        return str.__new__(cls, value.upper())


u = Upperstr("hello")
print(f"u={u}")
print(f"type(u)={type(u)}")
