#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 114
Встроенная функция enumerate
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-12"

x = [
    'one',
    'two',
    'three',
]

for index, value in enumerate(x):
    print(f"index={index}; value={value}")

iterator = enumerate(x)
print(f"iterator={iterator}")
print(f"{next(iterator)}")
print(f"{next(iterator)}")
print(f"{next(iterator)}")
try:
    print(f"{next(iterator)}")
except StopIteration as e:
    print(f"итератор закончился e={e}")


def countdown(n):
    while n > 0:
        yield n
        n -= 1


countdowner = countdown(3)
print(f"countdowner={countdowner}")
print(f"{next(countdowner)}")  # 3
print(f"{next(countdowner)}")  # 2
print(f"{next(countdowner)}")  # 1
try:
    print(f"{next(countdowner)}")
except StopIteration as e:
    print(f"итератор закончился e={e}")


def countdown2(n):
    i = 0  # iterations counter
    while n > 0:
        try:
            # print(f"inside countdowner2.gi_running={countdowner2.gi_running}")
            yield n
        except StopIteration as e:
            raise e  # does not work
        n -= 1
        i += 1


countdowner2 = countdown2(3)
# стр 83
# g.throw(exc [,exc_value [,exc_tb ]])
# Возбуждает исключение в функции-
# генераторе в точке вызова инструкции
# yield. exc – тип исключения, exc_value –
# значение исключения и exc_tb – необяза-
# тельный объект с трассировочной инфор-
# мацией. Если исключение перехвачено
# и обработано, вернет значение, переданное
# следующей инструкции yield
try:
    # print(f"countdowner2.gi_running={countdowner2.gi_running}")
    print(f"{next(countdowner2)}")
    # print(f"countdowner2.gi_running={countdowner2.gi_running}")
    print(f"{next(countdowner2)}")
    # print(f"countdowner2.gi_running={countdowner2.gi_running}")
    print(f"{next(countdowner2)}")
    # print(f"countdowner2.gi_running={countdowner2.gi_running}")
    print(f"{next(countdowner2)}")
    # print(f"countdowner2.gi_running={countdowner2.gi_running}")
except StopIteration as e:
    print(f"итератор 2 закончился={e}")
    # print(f"countdowner2.gi_running={countdowner2.gi_running}")

iterator2 = x.__iter__()
print(f"iterator2={iterator2}")
print(f"{next(iterator2)}")
print(f"{next(iterator2)}")
print(f"{next(iterator2)}")
try:
    print(f"{next(iterator2)}")
except StopIteration as e:
    print(f"iterator2 закончился e={e}")

iterator3 = range(3).__iter__()
print(f"iterator3={iterator3}")
print(f"{next(iterator3)}")
print(f"{next(iterator3)}")
print(f"{next(iterator3)}")
try:
    print(f"{next(iterator3)}")
except StopIteration as e:
    print(f"iterator3 закончился e={e}")

# x.append('four')
# for i, j in x:
#     print(f"i={i}, j={j}")
# ValueError: too many values to unpack (expected 2)

y = [
    'uno',
    'tuno',
    'tres',
    'quatro',
]

for i, j in zip(x, y):
    print(f"i={i}, j={j}")

x.append('four')
for i, j in zip(x, y):
    print(f"i={i}, j={j}")

for i in range(3):
    print(f"i={i}")  # после последней итерации будет вызван блок else
else:
    print(f"Цикл успешно завершен")

try:
    while True:
        raise Exception('проверка блока else в цикле while')
    else:
        print('цикл while успешно завершен')
except Exception as e:
    print('Выход из цикла while в результате исключения')

for i in []:
    print(f"i={i}")  # цикл без итераций вызовет блок else
else:
    print(f"цикл успешно завершен")

for i in x:
    print(f"i={i}")
    break  # не вызовет выполнение блока else
else:
    print(f"цикл успешно завершен")

try:
    print(f"I am trying")
except ValueError as e:
    print(f"value err")
else:
    print(f"no exceptions")
finally:
    print(f"finished")

try:
    print(f"I am trying")
    raise Exception('raise exception')
except Exception as e:
    print(f"except")
else:
    print(f"no exceptions")
finally:
    print(f"finished")

gena = countdown(3)
gena.close()
try:
    print(f"{next(gena)}")
except Exception as e:
    print(f"gena next failed e={e.__class__}")
