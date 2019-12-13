#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 43
Объекты и классы
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-06"

items = [37, 42]  # Создание списка объектов
items.append(73)  # Вызов метода append()
# Функция dir() выводит список всех методов объекта
print(f"methods of items={dir(items)}")
help(items.__add__)

items += [101]
print(f"methods of items={items}")


# пример простого класса стека
class Stack(object):
    def __init__(self):  # Инициализация стека
        self.stack = []

    def push(self, object):
        self.stack.append(object)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)


# пример использования класса стека
s = Stack()  # Создать стек
s.push("Dave")
s.push(42)
s.push([3, 5, 23])
print(f"stack = {s.stack}")
x = s.pop()  # переменная x получит значение [3,4,5]
print(f"x={x}")
y = s.pop()  # переменная y получит значение 42
print(f"y={y}")
del s  # Уничтожить объект s


# класс стека вариант 2 используя наследование
class Stack2(list):
    # Добавить метод push() интерфейса стека
    # Обратите внимание: списки уже имеют метод pop().
    def push(self, object):
        self.append(object)

    @staticmethod
    def example_static_method():
        print(f"hello from static method")


s2 = Stack2()  # Создать стек
s2.push("Dave")
s2.push(42)
s2.push([3, 5, 23])
print(f"stack2 = {s2}")
x2 = s2.pop()  # переменная x получит значение [3,4,5]
print(f"x2={x2}")
y2 = s2.pop()  # переменная y получит значение 42
print(f"y2={y2}")
s2.example_static_method()
del s2  # Уничтожить объект s
Stack2.example_static_method()


# объект Ellipsis стр 84
class Example(object):
    """
    Ellipse object example class
    """
    def __getitem__(self, item):
        """
        Фнукция индексирования [item]
        :param item:
        :return:
        """
        print(f"item={item}")
        return item


ex = Example()
ex[2]  # prints 2
ex[2, 3]  # prints (2,3)
ex[2, ..., 4]  # prints (2, Ellipsis, 4)


# страница 85 Создание и уничтожение объектов
class CreateExample(object):
    """
    Пример создания и уничтожения объектов
    2019-12-10
    """
    data = "data inited"

    def __new__(cls, *args, **kwargs):
        """
        Вызывается для создания нового экземпляра.
        :param args:
        :param kwargs:
        :return:
        """
        print(f"hello from new cls.data={cls.data}")

    def __init__(self):
        """
        Вызывается для инициализации нового экземпляра
        """
        print(f"hello from __init__ self.data={self.data}")

    def __del__(self):
        """
        Вызывается перед уничтожением нового экземпляра
        :return:
        """
        print(f"hello from __del__ self.data={self.data}")


ce = CreateExample()
del ce


# строковое представление объектов, стр 86
class StringObjects(object):
    """
    Пример строкового представления объектов
    2019-12-10
    """
    def __format__(self, format_spec):
        """
        Создает форматированное строковое представление
        :param format_spec:
        :return:
        """
        print(f"self.__format__ format_spec={format_spec}")
        return ""

    def __repr__(self):
        """
        Создает строковое представление объекта
        Метод __repr__() обычно возвращает строку с выражением, ко-
        торое может использоваться для воссоздания объекта с помощью функ-
        ции eval()
        :return:
        """
        print(f"self.__repr__")

    def __str__(self):
        """
        Создает простое строковое представление объекта
        :return:
        """
        print(f"self.__str__")


some_list = [1, 2, 3, 4, 5]
str_some_list = repr(some_list)
some_list2 = repr(str_some_list)
print(f"repr(some_list)={repr(some_list)}")
print(f"ellipsis list={[1, ..., 5]}")


class Sasha:
    username = None

    def __bool__(self):
        """
        Приведение объекта к двоичному типу
        :return: bool
        """
        if 'Sasha' in self.username:
            return True
        return False

