#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 29
Операции ввода вывода с файлами
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-05"

import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"script dir={dir_path}")

# open way 1
print("reading a file using way1")
with open(os.path.join(dir_path, "one-ten.txt"), "r") as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
print("")

# open way 2
print("readin a file using way2")
for line in open(os.path.join(dir_path, "one-ten.txt"), "r"):
    print(line, end='')
print("")

# write file way 1
print("writing a file using way1")
principal = 1000  # начальная сумма вклада
rate = 0.05  # процент
numyears = 5  # количество лет
year = 1
with open(os.path.join(dir_path, "write_test.txt"), "w") as f:
    while year <= numyears:
        principal = principal * (1 + rate)
        print(f"{year:03d} {principal:0.2f}", file=f)
        year += 1

# write file way 2
#todo problems with newlines!!!
year = 1
newline = ord("\n")
with open(os.path.join(dir_path, "write_test.txt"), "w") as f:
    while year <= numyears:
        principal = principal * (1 + rate)
        f.write(f"{year:03d} {principal:0.2f}{newline}")
        year += 1

# write file way 3
year = 1
newline = ord("\n")
with open(os.path.join(dir_path, "write_test.txt"), "w") as f:
    while year <= numyears:
        principal = principal * (1 + rate)
        f.write(f"{year:03d} {principal:0.2f}")
        f.write("\n")
        year += 1

# write file way 4
year = 1
newline = "\n"
with open(os.path.join(dir_path, "write_test.txt"), "w") as f:
    while year <= numyears:
        principal = principal * (1 + rate)
        f.write(f"{year:03d} {principal:0.2f}{newline}")
        year += 1

# stdin and stdout
sys.stdout.write("enter name:")
name = sys.stdin.readline()
print(f"hello {name}")
age = input("enter age:")
print(f"age is {age}")



