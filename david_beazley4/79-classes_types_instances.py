#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 76
Пользовательские функции
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-10"


class Foo:
    """
    Foo desc
    """
    pass


# класс сам по себе имеет тип type
print(f"type(Foo)={type(Foo)}")

# аттрибуты объекта типа type
print(f"type(Foo).__doc__={type(Foo).__doc__}")  # Строка документирования
print(f"type(Foo).__name__={type(Foo).__name__}")  # имя класса
print(f"type(Foo).__bases__={type(Foo).__bases__}")  # Кортеж с базовыми классами
print(f"type(Foo).__dict__={type(Foo).__dict__}")  # Словарь, содержащий методы и атрибуты класса
print(f"type(Foo).__module__={type(Foo).__module__}")  # Имя модуля, в котором определен класс
# print(f"type(Foo).__abstactmethods__={type(Foo).__abstractmethods__}")  # this code does not work
#  Множество имен абстрактных методов (может быть
# неопределен, если абстрактные методы отсутствуют
# в классе)

f = Foo()
print(f"type(f)={type(f)}")

# Аттрибуты экземпляра класса
print(f"f.__class__={f.__class__}")  # Класс, которому принадлежит экземпляр
print(f"f.__dict__={f.__dict__}")  # словарь содержащий данные экземляра

