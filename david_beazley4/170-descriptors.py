#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 170
Дескрипторы
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-16"

# 170 дескрипторы

# https://www.google.ru/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=2ahUKEwiK-POYiofnAhVFzqYKHZbfAXMQFjABegQICxAE&url=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%2594%25D0%25B5%25D1%2581%25D0%25BA%25D1%2580%25D0%25B8%25D0%25BF%25D1%2582%25D0%25BE%25D1%2580&usg=AOvVaw2EwDJTtBXpujtb5IgbjsML
# Дескриптор ...
# Дескри́птор (от лат. descriptor «описывающий») — лексическая единица (слово, словосочетание) информационно-поискового
# языка, служащая для описания основного смыслового содержания документа или формулировки запроса при поиске документа
# (информации) в информационно-поисковой системе.

# Дескриптор HTML — элемент языка разметки гипертекста HTML. В разговорной речи дескрипторы HTML называют тегами.
# Файловый дескриптор — число или структура, используемая в операционной системе для доступа к файлам, папкам, сокетам и т. п.

# https://pythonz.net/references/named/descriptor/
# Descriptor = Атрибут ОБЪЕКТА, доступ к которому подчиняется протоколу дескриптора



class TypedProperty:
    def __init__(self, name, type, default=None):
        self.name = f"_{name}"
        self.type = type
        self.default = default if default else type()
        print(f"in TypedPropery.__init__()\n\tself.name={self.name}\n\tself.type={self.type}\n\tself.default={self.default}")

    def __get__(self, instance, cls):
        """
        Позволяет определить значение, возвращаемое дескриптором.
        :param instance: Экземпляр класса владельца дескриптора, либо 'None', если обращаются в контексте класса, а не экземпляра.
        :param cls: Класс владельца дескриптора.
        :return:
        """
        print(f"in TypedPropery.__get__()\n\tself={self}\n\tinstance={instance}\n\tcls={cls}\n\tself.name={self.name}\n\tself.default={self.default}")
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        print(f"in TypedPropery.__set__()\n\tself={self}\n\tinstance={instance}\n\tvalue={value}\n\tself.name={self.name}\n\tself.default={self.default}")
        if not isinstance(value, self.type):
            raise TypeError(f"Значение должно быть типа {self.type}")
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Невозможно удалить аттрибут")


print(f"before declaration Foo class")


class Foo:
    name = TypedProperty("name", str)
    num = TypedProperty("num", int, 42)


print(f"class Foo has declared\n")

print(f"исследование класса Foo")
# Foo.name = 'ivan'  # выполнение данной инструкции свяжет Foo.name с 'ivan'
print(f"Foo.name={Foo.name}")  # если раскомментировать Foo.name='ivan' НЕ будет вызов TypedProperty.__get__
print(f"Foo.num={Foo.num}")  # произойдет вызов TypedProperty.__get__(self=объект TypedProperty, instance=None, cls=Foo)
print(f"конец исследования класса Foo\n")

print(f"Исследование экземпляра Foo")
foo = Foo()
print(f"экземляр Foo создан")
print(f"foo.__dict__={foo.__dict__}")
print(f"foo.name={foo.name}")
foo.name = 'bobo'  # создаст переменную foo._name == 'bobo', вызовет TypedProperty.__set__(self=объект TypedProperty, instance=объект Foo, value='bobo')
print(f"foo.__dict__={foo.__dict__}")
print(f"foo.name={foo.name}")
print(f"конец исследования экземпляра Foo\n")