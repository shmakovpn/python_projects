#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 99
Операции над последовательностями
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-11"

print(f"конка+тенация={'конка' + 'тенация'}")
print(f"[1,2,3]+[4,5]={[1, 2, 3] + [4, 5]}")  # при этом выполняется лишь поверхносное копирование
print(f"hello*3={'hello' * 3}; 3*hello={3 * 'hello'}")
print(f"[1,2]*3={[1, 2] * 3}; 3*[1,2]={3 * [1, 2]}")
a, b = 'ab'
print(f"a={a}, b={b}")
for i in 'hello':
    print(f"i={i}")
print(f"sum([1,2,3])={sum([1, 2, 3])}")
# print(f"sum('hello')={sum('hello')}") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

a = [3, 4, 5]
b = [a]
c = 4 * b
print(f"c={c}")
a[0] = -7
print(f"c={c}")

print(f"[1,2,3][-1]={[1, 2, 3][-1]}")  # 3

a = [3, 4, 5]
try:
    a[3] = 4
except IndexError as e:
    print(f"произошел выход индекса за пределы последовательности")

try:
    a[0:1] = 90
    print(f"a={a}")
except TypeError as e:
    print(f"срезу можно присвоить только итерируемый объект")

a[0:2] = [32, 33]
print(f"a={a}")
a[0:1] = ['a', 'b', 'c']
print(f"a={a}")
a[:] = [767]
print(f"a={a}")

s = list('I have a pen')
s[8:9] = list(' big ')
print(f"s={''.join(s)}")

print(f"total: {231.54768:+010.2f}")

print(f"vars()={vars()}")
