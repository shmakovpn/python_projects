#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 158
Инструкция class
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-14"

import random


# class A:
#     x = 'hello'
#     print(f"inside class A")
#
#     def __init__(self):
#         print(f"hello from A __init__")
#
#
# class B(A):
#     y = 'I am B'
#     print(f"inside class B")
#
#     def __init__(self):
#         print(f"hello from B __init__")
#         # super(B, self).__init__()  # python 2
#         super().__init__()  # python 3
#
#
# a = A()
# b = B()

# 158
class Account(object):
    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    def deposit(self, amt):
        """
        Взнос
        :param amt:
        :return:
        """
        self.balance = self.balance + amt

    def withdraw(self, amt):
        """
        Снять со счета
        :param amt:
        :return:
        """
        self.balance = self.balance - amt

    def inquiry(self):
        """
        Узнать баланс
        :return:
        """
        return self.balance

    print(f"class Account:\n\tdeposit={deposit}\n\twithdraw={withdraw}\n\tinquiry={inquiry}")


# 161 злой аккаунт
class EvilAccount(Account):
    def __init__(self, name, balance, evilfactor):
        # super(EvilAccount, self).__init__(name, balance)
        Account.__init__(self, name, balance)
        self.evilfactor = evilfactor

    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * self.evilfactor  # Внимание: патентуем идею
        else:
            return self.balance

    print(f"class EvilAccount(Account):\n\t__init__={__init__}\n\tinquiry={inquiry}")


# 163 множественное наследование
class DepositCharge(Account):
    fee = 5.00

    def deposit_fee(self):
        print(f"in DepositCharge.deposit_fee(self) self.withdraw.__func__={self.withdraw.__func__}; self.fee={self.fee}")
        print(f"super().withdraw.__func__={super().withdraw.__func__}")
        # Account.withdraw(self, self.fee)  # будет работать
        super().withdraw(self.fee)
        # self.withdraw(self.fee) # вызовет ошибку RecursionError: maximum recursion depth exceeded while calling a Python object

    print(f"class DepositCharge:\n\tfee={fee}\n\tdeposit_fee={deposit_fee}")


class WithdrawCharge(Account):
    fee = 2.5

    def withdraw_fee(self):
        print(f"in WithdrawCharge.withdraw_fee(self) self.withdraw.__func__={self.withdraw.__func__}; self.fee={self.fee}")
        # Account.withdraw(self, self.fee)  # будет работать
        super().withdraw(self.fee)
        # self.withdraw(self.fee)  # вызовет ошибку RecursionError: maximum recursion depth exceeded while calling a Python object

    print(f"class WithdrawCharge:\n\tfee={fee}\n\twithdraw_fee={withdraw_fee}")


# Класс, использующий механизм множественного наследования
class MostEvilAccount(EvilAccount, DepositCharge, WithdrawCharge):
    def deposit(self, amt):
        self.deposit_fee()
        super(MostEvilAccount, self).deposit(amt)

    def withdraw(self, amt):
        self.withdraw_fee()
        super(MostEvilAccount, self).withdraw(amt)

    print(f"class MostEvilAccount:\n\tdeposit={deposit}\n\twithdraw={withdraw}")


d = MostEvilAccount("Dave", 500.00, 1.10)
print(f"d.deposit.__func__={d.deposit.__func__}")
print(f"d.withdraw.__func__={d.withdraw.__func__}")
print(f"MostEvilAccount.__mro__={MostEvilAccount.__mro__}")
d.deposit_fee()  # Вызовет DepositCharge.deposit_fee(). fee == 5.00
d.withdraw_fee()  # Вызовет WithdrawCharge.withdraw_fee(). fee == 5.00 ??


class Baba(object):
    def go(self):
        print(f"go Baba go!!")


class Mama(Baba):
    def go(self):
        print(f"go Mama go!!")

    def go_mama(self):
        self.go()


class Docha(Mama):
    def go(self):
        print(f"go Docha go!!")


docha = Docha()
docha.go_mama()