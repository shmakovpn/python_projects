#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 74
Методы и операторы, поддерживаемые множествами
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"


s = {'one', 'two', 'three'}  # the same as set([])
print(f"type(s)={type(s)}")
print(f"len(s)={len(s)}")
try:
    s2 = {'x1', ['a', 'b'], 'y'}
except TypeError as e:
    print(f"во множество могут входить только изменяемые объекты e={e}")
x = {'two', 'three', 'four'}
print(f"s.difference(x)={s.difference(x)}")
print(f"x.difference(s)={x.difference(s)}")
print(f"s.intersection(x)={s.intersection(x)}")
print(f"s.isdisjoint(x)={s.isdisjoint(x)}")  # Пересечение множеств. Возвращает все элементы, присутствующие в обоих
# множествах s и t.
y = {'two', 'one'}
print(f"y.issubset(s)={y.issubset(s)}")
print(f"s.issuperset(y)={s.issuperset(y)}")
print(f"s.symmetric_difference(x)={s.symmetric_difference(x)}")
print(f"s.union(x)={s.union(x)}")
s.add('nine')
print(f"s={s}")
y.clear()
print(f"y={y}")
s.difference_update(x)
print(f"s={s}")
s.discard('one')
print(f"s={s}")
x.intersection_update(s)
print(f"x={x}")
s = {'one', 'two', 'three'}  # the same as set([])
x = {'two', 'three', 'four'}
print(f"x.pop()={x.pop()}")
s.symmetric_difference_update(x)
print(f"s={s}")
s.update(x)
print(f"s={s}")
