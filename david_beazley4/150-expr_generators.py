#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 150
Выражения генераторы
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-10"

import os
SCRIPT_DIR = os.path.dirname(__file__)

a = [1, 2, 3, 4]
print(f"a={a}")
b = (10*i for i in a)
print(f"b={b}")  # generator object
print(f"next(b)={next(b)}")  # 10
print(f"next(b)={next(b)}")  # 20
print(f"next(b)={next(b)}")  # 30
b_list = [10*i for i in a]
print(f"b_list={b_list}")  # [10, 20, 30, 40]

# пример чтения файла
filename = os.path.join(SCRIPT_DIR, "one-ten.txt")
f = open(filename)
lines = (t.strip() for t in f)
print(f"lines={lines}")
for line in lines:
    print(f"line={line}")


fields = (line.split() for line in open(os.path.join(SCRIPT_DIR, "portfolio.txt")))
print(sum(float(f[1])*float(f[2]) for f in fields))
print(f"fields={fields}")

# SELECT аналог пример
print(f"select example 1")
fields = (line.split() for line in open(os.path.join(SCRIPT_DIR, "portfolio.txt")))
portfolio = [{
    'name': f[0],
    'shares': int(f[1]),
    'price': float(f[2])
} for f in fields]
# несколько запросов
msft = [s for s in portfolio if s['name']=="MSFT"]
print(f"msft={msft}")
large_holdings = [s for s in portfolio if s['shares']*s['price']>=10000]
print(f"large_holdings={large_holdings}")

# SELECT аналог пример
fields = (line.split() for line in open(os.path.join(SCRIPT_DIR, "portfolio.txt")))
portfolio = ({
    'name': f[0],
    'shares': int(f[1]),
    'price': float(f[2])
} for f in fields)
# несколько запросов
msft = (s for s in portfolio if s['name']=="MSFT")
print(f"msft={msft}")
large_holdings = (s for s in portfolio if s['shares']*s['price'] >= 10000)
print(f"large_holdings={large_holdings}")
msft = list(msft)
large_holdings = list(large_holdings)  # посто так данные выбраны из генератора portfolio
print(f"msft={msft}")
print(f"large_holdings={large_holdings}")
