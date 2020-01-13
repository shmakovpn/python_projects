#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 148
Генераторы списков
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-09"

nums = [1, 2, 3, 4, 5, ]
squares = []
for n in nums:
    squares.append(n * n)
squares2 = [n * n for n in nums]
print(f"squares2={squares2}")

# 149
# Для иллюстрации ниже приводится несколько примеров:
a = [-3, 5, 2, -10, 7, 8]
b = 'abc'
print(f"a={a}")
print(f"b={b}")
print(f"[2*s for s in a]={[2 * s for s in a]}")
print(f"[s for s in a if s >= 0]={[s for s in a if s >= 0]}")
print(f"[(x,y) for x in a for y in b if x > 0 ]={[(x, y) for x in a for y in b if x > 0]}")
# это эквивалент
result = []
for x in a:
    for y in b:
        if x > 0:
            result.append((x, y,))
print(f"result={result}")

f = [(1, 2), (3, 4), (5, 6)]
print(f"f={f}")
print(f"[ math.sqrt(x*x+y*y) ")

