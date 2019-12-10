#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 58
Идентичность и тип объекта
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"


# Сравнение двух объектов
def compare(a, b):
    if a is b:
        # a и b ссылаются на один и тот же объект
        print(f"a и b ссылаются на один и тот же объект")
    if a == b:
        # объекты a и b имеют одинаковые значения
        print(f"объекты a и b имеют одинаковые значения")
    if type(a) is type(b):
        # объекты a и b имеют один и тот же тип
        print(f"объекты a и b имеют один и тот же тип")


compare(1, "1")  # prints nothing
compare(1, 2)  # объекты a и b имеют один и тот же тип
compare(1, 1)  # a и b ссылаются на один и тот же объект, объекты a и b имеют одинаковые значения, объекты a и b имеют один и тот же тип


class Foo:
    pass


x = Foo()
print(f"x is Foo={x is Foo}")
print(f"x is object={x is object}")
print(f"type(x) is Foo={type(x) is Foo}")
print(f"type(x) is objects={type(x) is object}")
print(f"isinstance(x, Foo)={isinstance(x, Foo)}")
print(f"isinstance(x, object)={isinstance(x, object)}")
