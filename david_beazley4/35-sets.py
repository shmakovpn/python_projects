#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 35
Множества
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-05"

s = set([3, 5, 9, 10, 5, ])  # Создаст множество чисел
t = set("Hello")   # Создаст множество уникальных символов

print(f"set of unique numbers: {s}")
print(f"set pf unique symbols: {t}")


a = t | s # Объединение t и s
print(f"a={a}")
b = t & s  # Пересечение t и s
print(f"b={b}")
c = t - s  # Разность (элементы, присутствующие в t, но отсутствующие в s)
print(f"c={c}")
d = t ^ s  # Симметричная разность (элементы, присутствующие в t или в s, но не в двух множествах сразу)
print(f"d={d}")

t.add("x")           # Добавит единственный элемент
print(f"t={t}")
s.update([10, 37, 42, ])  # Добавит несколько элементов в множество s
print(f"s={s}")

t.remove("H")  # удалить элемент из множества
print(f"t={t}")

sb = set([('go', 'home'), ('shut', 'down')])
print(f"sb={sb}")

# list of keys of dict
prices = {
    "GOOG" : 490.10,
    "APPL" : 123.50,
    "IBM": 91.50,
    "MSFT": 52.13
}

print(f"list keys={list(prices)}")
print(f"tuple keys={tuple(prices)}")

