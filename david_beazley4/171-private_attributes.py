#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 171
Инкапсуляция данных и частные атрибуты
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-16"


class A:
    def __init__(self):
        self.__X = 3

    def __spam(self):  # Будет изменено на _A__spam()
        print(f"in A.__spam")

    def bar(self):
        self.__spam()


class B(A):
    def __init__(self):
        A.__init__(self)
        self.__X = 37

    def __spam(self):
        print(f"in B.__spam")


a = A()
# print(f"a.__X={a.__X}")  # вызовет ошибку: AttributeError: 'A' object has no attribute '__X'
print(f"a._A__X={a._A__X}")  # prints 3

b = B()
print(f"b._B__X={b._B__X}")
print(f"b._A__X={b._A__X}")




class C(B):
    _C__X = 'hello'
    _C__Y = 'hello y'

    def __init__(self):
        B.__init__(self)
        self.__X = 345
        print(f"in C.__init__(): __Y={self.__Y}")  # prints 'hello y'


c = C()
print(f"c._C__X={c._C__X}")  # prints 345
print(f"c.__dict__={c.__dict__}")  # {'_A__X': 3, '_B__X': 37, '_C__X': 345}
print(f"dir(c)={dir(c)}")  # ['_A__X', '_B__X', '_C__X', '_C__Y', '__class__', '__delattr__', '__dict__', '__dir etc.
c.bar()  # calls A.__spam