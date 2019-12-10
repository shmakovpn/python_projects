#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 72
Отображения (словари)
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"


s = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
}

print(f"len(s)={len(s)}")
s.clear()
print(f"len(s)={len(s)}")

d = {
    'aa': 'hello',
    'bb': ['one', 'two', ],
    'cc': 'yy',
}

d2 = d.copy()
d2['bb'][1] = 'test'
print(f"d={d}")  # {'aa': 'hello', 'bb': ['one', 'test'], 'cc': 'yy'}
print(f"s.get('eleven')={s.get('eleven', 11)}")
print(f"d.setdefault('eleven', 11)={d.setdefault('eleven', 11)}")
print(f"d.setdefault()={d['eleven']}")
print(f"d.items()={d.items()}")  # возвращает итератор
print(f"d.keys()={d.keys()}")  # возвращает итератор
print(f"d.values()={d.values()}")  # возвращает итератор
a = ['a1', 'a2', 'a3']
print(f"d.fromkeys(a)={d.fromkeys(a)}")


