#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 62
Объкты первого класса
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"
import math

# Все объекты в языке Python могут быть отнесены к объектам первого класса.
# Это означает, что все объекты, имеющие идентификатор, имеют одина-
# ковый статус.
# Это также означает, что все объекты, имеющие идентификатор, можно интерпретировать, как данные.

items = {
    "number": 42,
    "text": "hello world",
}
print(f"items={str(items)}")

# «Первоклассную» природу объектов можно наблюдать,
# если попробовать добавить в этот словарь несколько необычных элементов.
items["func"] = abs  # Добавляется функция abs()
items["mod"] = math  # Добавляется модуль
items["error"] = ValueError  # Добавляется тип исключения
nums = [1, 2, 3, 4]
items["append"] = nums.append  # Добавляется метод другого объекта
print(f"items={str(items)}")
# При желании можно обратиться к элементам сло-
# варя вместо оригинальных объектов, и такой код будет работать.
print(f"items['func'](-45)={items['func'](-45)}")
print(f"items['mod'].sqrt(4)={items['mod'].sqrt(4)}")
try:
    x = int("a lot")
except items['error'] as e:
    print(f"could not convert: {e}")
items["append"](100)
print(f"nums={nums}")

line = "GOOG,100,490.10"
field_types = [str, int, float]
raw_fields = line.split(',')
fields = [ty(val) for ty, val in zip(field_types, raw_fields)]
print(f"fields={fields}")

for i in zip("hello", "world"):
    print(f"i={i}")

for i in zip(field_types, raw_fields):
    print(f"i={i}")

a2 = ['one', 'two']
a3 = ['eleven', 'twelve', '13']
zip23 = zip(a2, a3)
for i in zip23:
    print(f"i={i}")
