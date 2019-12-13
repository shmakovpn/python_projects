#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Разложение числа на просты множители
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-13"

num = 1773682
divider = 2
result = []
while num > 1:
    if not num % divider:
        result.append(divider)
        num //= divider
    else:
        divider += 1

test = 1
for i in result:
    test *= i

print(f"result={result}, test={test}")
