#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 25
Вычисление сложных процентов. Листинг 1.1
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-05"

from datetime import datetime

today = datetime.now()
print(f"{today:%Y-%m-%d %H:%M:%S}")

principal = 1000  # начальная сумма вклада
rate = 0.05  # процент
numyears = 5  # количество лет
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    # print("%03d %0.2f" % (year, principal))
    print(f"{year:03d} {principal:0.2f}")
    year += 1
