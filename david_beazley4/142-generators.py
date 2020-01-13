#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 142
Генераторы
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-17"


def countdown(n):
    print(f"обратный отсчет от n={n}")
    while n > 0:
        yield n
        n -= 1


for i in countdown(4):
    print(f"i={i}")

print(f"sum(countdown(4)={sum(countdown(4))}")

list4 = [x for x in countdown(4)]
print(f"list4={list4}")

list4i = [(i, x) for (i, x) in enumerate(countdown(4))]
print(f"list4i=={list4i}")


cd = countdown(10)
next(cd)
cd.close()
try:
    next(cd)
except StopIteration as e:
    print(f"перехвачено StopIteration e={e}")


def countdown2(n):
    print(f"Обратный отсчет2, начиная с n={n}")
    try:
        while n > 0:
            yield n
            n -= 1
    except GeneratorExit:
        print(f"Достигнуто значение n={n}")


cd2 = countdown2(10)
print(f"{next(cd2)}")
print(f"{next(cd2)}")
cd2.close()


# 143 Сопрограммы и выражения yield
def receiver():
    print(f"receiver готов к приему значений")
    while True:
        n = (yield)
        print(f"Получено {n}")

r = receiver()
next(r)  # Выполнить до первой инструкции yield
r.send('hello')
r.send('world')


def coroutine(func):
    def start(*args, **kwargs):
        print(f"создадим сопрограмму {func.__name__}")
        g = func(*args, **kwargs)
        print(f"выполним next({func.__name__})")
        next(g)
        return g
    return start


@coroutine
def receiver2():
    print(f"receiver2 готов к приему значений")
    n = 0
    try:
        while True:
            print(f"было {n}")
            try: 
                n = (yield n)
                print(f"получено значение {n}")
            except RuntimeError as e:
                print("RuntimeError")
    except GeneratorExit:
        print(f"прием завершен")


r = receiver2()
r.send('hello2')
print(f"r.send('world2')={r.send('world2')}")
print(f"r.throw={r.throw(RuntimeError, 'вас надули')}")


@coroutine
def line_splitter(delimiter=None):
    print(f"Все готово к разбиению строки")
    result = None
    line = None
    while True:
        print(f"--> перед yield result={result}, line={line}")
        line = (yield result)
        print(f"--> после yield result={result}, line={line}")
        result = line.split(delimiter)


print("")
print(f"проверяем line_splitter")
s = line_splitter(',')
print(f"s.send('a,b,c')")
print(f"{s.send('a,b,c')}")
print(f"s.send('100,200,300')")
print(f"{s.send('100,200,300')}")
