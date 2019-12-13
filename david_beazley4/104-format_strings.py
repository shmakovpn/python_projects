#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 104
Форматирование строк
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-12"

# Таблица 4.1. Спецификаторы формата стр 104
# d, i Целое или длинное целое десятичное число.
print(f"129484373:d={129484373:d}")
# print(f"129484373:i={129484373:i}")  # does not work
print("%i" % 129484373)  # works
# print("%{0:i}".format(129484373)) does not work

# u - Целое или длинное целое число без знака.
# print(f"-121:u={(-121):u}") # does not work
x = -121
print("%u" % x)  # работает, но все равно выдает результат со знаком

# o - Целое или длинное целое восьмеричное число.
print(f"9:o={9:o}")

# x - Целое или длинное целое шестнадцатеричное число.
print(f"254:x={254:x}")
# X - Целое или длинное целое шестнадцатеричное число (с символами в верхнем регистре).
print(f"254:X={254:X}")

# f Число с плавающей точкой в формате [-]m.dddddd
print(f"132.3893:f={132.3893:f}")
try:
    print(f"132.3893:d={132.3893:d}")
except ValueError as e:
    print(f"невозможно вывести float используя спецификатор d e={e}")
print(f"13.67:.f={13.67:.0f}")  # если надо вывести число с плавающей точкой как целое
print(f"0.5:.f={0.5:.0f}")  # python3 округляет 0.5 до 0 !!!
print(f"round(0.5)={round(0.5)}")  # python3 округляет 0.5 до 0 !!!
print(f"{132:f}")  # вывести целое как float

# вывод в двоичном формате
print(f"7:b={7:b}")


# e - Число с плавающей точкой в формате [-]m.dddddde ± xx.
print(f"(255**15):e={(255 ** 15):e}")
print(f"12:e={12:e}")
print(f"2:e={2:e}")
# E - Число с плавающей точкой в формате [-]m.ddddddE ± xx.
print(f"(255**15):E={(255 ** 15):E}")
# g, G - Использует спецификатор %e или %E, если экспонента меньше
# -4 или больше заданной точности; в противном случае исполь-
# зует спецификатор %f .
print(f"(255**15):g={(255 ** 15):g}")
print(f"(255**15):G={(255 ** 15):G}")
print(f"12:g={12:g}")

# s - Строка или любой объект. Для создания строкового пред-
# ставления объектов используется функция str().
print(f"{'go go go':s}")
try:
    print(f"{12:s}")
except ValueError as e:
    print(f"невозможно использовать целое число со спецификатором s")


class Stest:
    def __str__(self):
        return 'hello from __str__'

    def __repr__(self):
        return 'hello from __repr__'

    def __format__(self, format_spec):
        print(f"format_spec={format_spec}")
        if 's' in format_spec:
            return str(self)
        elif 'r' in format_spec:
            return repr(self)
        else:
            raise ValueError(f"спецификатор формата '{format_spec}' не поддерживается")


s_test = Stest()
try:
    print(f"s_test:s={s_test:s}")
except ValueError as e:
    print("не так все просто e={e}")

print(f"s_test:r={s_test:r}")  # вызывается функция __format__ в которую я прописал вызов

try:
    print(f"s_test:d={s_test:d}")
except ValueError as e:
    print(f"ошибка e={e}")

# c - Единственный символ.
print(f"goo:c={ord('a'):c}")

# % - Символ %.
print("%")
print("%% %s" % "test %")

print(f"total: {231.54768:+010.2f}")
print(f"total: {-231.54768:+010.2f}")
print(f"total: {231.54768: 010.2f}")  # добавление пробела вместо знака
print(f"total: {3:<06d}")  # выравнивание по левому краю и заполнение нулями
print(f"total: {3:>06d}")  # выравнивание по правому краю и заполнение нулями
print(f"total: {3:^06d}")  # выравнивание по середине и заполнение нулями
print(f"total: {3:=^6d}")  # выравнивание по середине и =
print(f"total: {3:#^6d}")  # выравнивание по середине и #
print(f"{0.25:.0%}")  # вывод процентов


print(f"vars()={vars()}")
