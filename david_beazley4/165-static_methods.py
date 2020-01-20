#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 165
Статические методы и методы классов
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-15"

import time
import math


class Foo:
    @staticmethod
    def add(x, y):
        return x + y


print(f"Foo.add(3,4)={Foo.add(3,4)}")


# 166
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_yday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_yday)

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"


# несколько примеров создания экземпляров
a = Date(1967, 4, 9)
print(f"Date(1967, 4, 9)={Date(1967, 4, 9)}")
b = Date.now()
print(f"Date.now={Date.now()}")
c = Date.tomorrow()
print(f"Date.tomorrow={Date.tomorrow()}")


# методы класса
class Times:
    factor = 1
    @classmethod
    def mul(cls, x):
        return cls.factor * x


class TwoTimes(Times):
    factor = 2


print(f"TwoTimes.mul()={TwoTimes.mul(4)}")  # will print 8: Times.mull(TwoTimes, 4)

# существуют практические, и весьма тонкие, применения методов классов
class EuroDate(Date):
    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"


# поведение методов now() и tomorrow() будет немного портить об-
# щую картину.
# если вызвать метод EuroDate.now(), вместо объекта
# EuroDate он вернет объект Date
class Date2:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def now(cls):
        t = time.localtime()
        # создать объект соотстветствующего типа
        return cls(t.tm_year, t.tm_mon, t.tm_yday)


# свойства
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi*self.radius**2

    @property
    def perimeter(self):
        return 2*math.pi*self.radius


circle = Circle(4)
print(f"circle.area={circle.area}")

try:
    circle.perimeter = 4
except AttributeError as e:
    print(f"e={e}")


# 169 свойства, геттеры и сеттеры
class Foo:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise TypeError(f"имя должно быть строкой!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError(f"Невозможно удалить аттрибут name")


f = Foo("Gvido")
print(f"f.name={f.name}")
f.name = "Monti"
print(f"f.name={f.name}")
try:
    f.name = 45
except TypeError as e:
    print(f"f.name=45 -> e={e}")

try:
    del f.name
except TypeError as e:
    print(f"del f.name -> e={e}")





