#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 64
Последовательности
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"

s = "Операции, общие для всех типов последовательностей"
print(f"s[4]={s[4]}")
print(f"s[2:8]={s[2:8]}")
print(f"s[2:13:3]={s[2:13:3]}")
print(f"len(s)={len(s)}")
print(f"min(s)={min(s)}")  # пробел
print(f"max(s)={max(s)}")  # я
print(f"all(x)={all(s)}")  # True
print(f"any(x)={any(s)}")  # True
try:
    print(f"sum(s)={sum(s)}")
except TypeError as e:
    print(f"операция sum не поддерживается строковыми последовательностями e={e}")
x = [1, 2, 0, 80, 34, 23, 24, 55, ]
print(f"all(x)={all(x)}")  # False: 0 in x - в двоичной интерпритации это False,
print(f"any(x)={any(x)}")  # True
try:
    del s[1]
except TypeError as e:
    print(f"del не работает со строками e={e}")
print(f"s={s}")

del x[0]
print(f"x={x}")
del x[3:5]
print(f"x={x}")
del x[1::2]
print(f"x={x}")

slist = list(s)
print(f"slist={slist}")
del slist[2:37:4]
print(f"slist={slist}")
print(f"s.index('ц')={s.index('ц')}")
try:
    print(f"s.index('ъ')={s.index('ъ')}")
except ValueError as e:
    print(f"в строке нет буквы 'ъ' e={e}")
slist.remove('ц')
print(f"slist={slist}")
x.extend([99, 88, 77, 66, ])
print(f"x={x}")
slist.sort()
print(f"slist={slist}")
slist.reverse()
print(f"slist={slist}")
x.insert(1, "hello")
print(f"x={x}")
print(f"x.pop[1]={x.pop(1)}")
print(f"x={x}")
x.remove(88)
print(f"x={x}")
x.sort(reverse=True)
print(f"x={x}")


def mod(num):
    return num % 10


x.sort(key=mod, reverse=False)
print(f"x={x}")
x.append(7)
x.sort(key=mod, reverse=False)
print(f"x={x}")


