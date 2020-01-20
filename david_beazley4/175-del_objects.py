#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 175
Управление памятью объектов (как работает удаление объектов)
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-16"

import weakref


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.observers = set()  # пустое множество

    def __del__(self):
        print(f"in Account.__del__")
        for ob in self.observers:
            ob.close()
        del self.observers
        print(f"end Account.__del__")

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        print("in Account.unregister()")
        if hasattr(self, 'observers'):
            self.observers.remove(observer)

    def notify(self):
        for ob in self.observers:
            ob.update()

    def withdraw(self, amt):
        self.balance -= amt
        self.notify()


class AccountObserver:
    def __init__(self, theaccount):
        self.accountref = weakref.ref(theaccount)  # Создаст слабую ссылку
        theaccount.register(self)

    def __del__(self):
        acc = self.accountref()  # Вернет объект счета
        if acc:
            acc.unregister(self)

    def update(self):
        print(f"balance: {self.accountref().balance:0.2f}")

    def close(self):
        print(f"наблюдение за счетом окончено")


# Пример создания
a = Account('Dave', 1000.00)
a_ob = AccountObserver(a)

print(f"a.__dict__={a.__dict__.keys()}")
print(f"a.__dir__()={a.__dir__()}")


class A:
    x = 2

    def __setattr__(self, key, value):
        print(f"in A.__setattr__ key={key}, value={value}")
        super().__setattr__(key, value)

a = A()
a.x = 3
