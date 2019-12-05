#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 33
Дополнительные особенности списков
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-05"

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"script dir={dir_path}")

with open(os.path.join(dir_path, "one-ten-nums.txt"), "r") as f:
    lines = f.readlines()

# Преобразовать все значения из строк в числа с плавающей точкой
fvalues = [float(line) for line in lines]

# Вывести минимальное и максимальное значения
print(f"minimum: {min(fvalues)}")
print(f"maximum: {max(fvalues)}")

# или так
fvalues = [float(line) for line in open(os.path.join(dir_path, "one-ten-nums.txt"), "r")]
# Вывести минимальное и максимальное значения
print(f"minimum: {min(fvalues)}")
print(f"maximum: {max(fvalues)}")


list1 = ['one', 'two', 'three',]
item1, item2, item3 = list1
print(f"item1={item1}, item2={item2}, item3={item3}")

# _ переменная аля, /dev/null
list2 = ['one', 'two', 'three', 'four']
item1, item2, item3, _ = list2
print(f"item1={item1}, item2={item2}, item3={item3}")