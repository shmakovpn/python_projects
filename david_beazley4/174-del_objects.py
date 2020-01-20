#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 174
Управление памятью объектов (как работает удаление объектов)
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-16"

import os
import psutil
import resource

print(f"resource.getrusage(resource.RUSAGE_SELF)={resource.getrusage(resource.RUSAGE_SELF)}")
process = psutil.Process(os.getpid())
memory1 = process.memory_info().rss
print(process.memory_info().rss / (1024 * 1024))  # in bytes


# x = [i for i in range(10**8)]
# print(f"resource.getrusage(resource.RUSAGE_SELF)={resource.getrusage(resource.RUSAGE_SELF)}")
# process = psutil.Process(os.getpid())
# print(process.memory_info().rss/(1024*1024))  # in bytes


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
        self.theaccount = theaccount
        theaccount.register(self)

    def __del__(self):
        print(f"in AccountObserver.__del__")
        self.theaccount.unregister(self)
        del self.theaccount
        print(f"end AccountObserver.__del__")

    def update(self):
        print(f"balance: {self.theaccount.balance:0.2f}")

    def close(self):
        print(f"наблюдение за счетом закончено")


# Пример создания
a = Account('Dave', 1000.00)
a_ob = AccountObserver(a)
