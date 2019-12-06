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
