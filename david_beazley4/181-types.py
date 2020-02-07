#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 181
Типы и проверка принадлежности к классу
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-24"


class IClass:
    def __init__(self):
        self.implementors = set()

    def register(self, C):
        self.implementors.add(C)

    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return any(c in self.implementors for c in subclass.mro())


class Foo:
    def spam(self, a, b):
        pass


class FooProxy:
    def __init__(self, f):
        self.f = f

    def spam(self, a, b):
        return self.f.spam(a, b)


# пример использования
IFoo = IClass()
IFoo.register(Foo)
IFoo.register(FooProxy)

f = Foo()
g = FooProxy(f)
print(f"isinstance(f, IFoo)={isinstance(f, IFoo)}")
print(f"isinstance(g, IFoo)={isinstance(g, IFoo)}")
print(f"issubclass(FooProxy, IFoo)={issubclass(FooProxy, IFoo)}")

from abc import ABCMeta, abstractmethod, abstractproperty


#class Foo3:
class Foo3(metaclass=ABCMeta):
    #__metaclass__ = ABCMeta

    @abstractmethod
    def spam(self, a, b):
        pass

    @property
    @abstractmethod
    def some(self):
        pass

    # @abstractproperty
    # def name(self):
    #     pass

    # @abstractmethod
    # @property
    # def bar(self):
    #     pass

try:
    x = Foo3()
except TypeError as e:
    print(f"e={e}")  # e=Can't instantiate abstract class Foo3 with abstract methods some, spam


# 185 создание класса "вручную"
class_name = "Foo4"  # имя класса
class_parameters = (object, )  # базовые классы
class_body = """
def __init__(self, x):
    self.x = x

def blah(self):
    print("Hello world")
"""
class_dict = {}

# Выполнить тело класса с использованием локального словаря class_dict
exec(class_body, globals(), class_dict)

# создать объект класса Foo4
Foo4 = type(class_name, class_parameters, class_dict)
xx = Foo4(34)


# 186 использование метаклассов
# классы созданные с использованием данного метакласса должны содержать строки документирования своих методов
class DocMeta(type):
    def __init__(self, name, bases, dict):
        for key, value in dict.items():
            # Пропустить специальные и частные методы
            if key.startswith("__"):
                continue
            # Пропустить любые невызываемые объекты
            if not hasattr(value, "__call__"):
                continue
            # Проверить наличие строки документирования
            if not getattr(value, "__doc__"):
                raise TypeError(f"'{key}' must have a docstring")
        type.__init__(self, name, bases, dict)  # вызов конструктора родительского класса


class TestDocMeta(metaclass=DocMeta):

    def hello(self):
        """
        some doc of hello
        :return:
        """
        print("hello")


try:
    class TestDocMeta2(metaclass=DocMeta):
        def hello(self):
            print("hello")
except TypeError as e:
    print(f"e={e}")  # e='hello' must have a docstring


# 187 пример с использование дескрипторов
class TypedProperty:
    def __init__(self, type, default=None):
        self.name = None
        self.type = type
        if default:
            self.default = default
        else:
            self.default = type()

    def __get__(self, instance, owner):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"Значение должно быть типа '{self.type}'")
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError(f"невозможно удалить аттрибут")

# в данном примере аттрибуту 'name' декриптора просто присваивается значение None.
# Заполнение этого аттрибута будет поручено метаклассу.

class TypedMeta(type):
    def __new__(cls, name, bases, dict):
        slots = []
        for key, value in dict.items():
            if isinstance(value, TypedProperty):
                value.name = f"_{key}"
                slots.append(value.name)
        dict['__slots__'] = slots
        return type.__new__(cls, name, bases, dict)


# Базовый класс для объектов, определяемых пользователем
class Typed(metaclass=TypedMeta):
    pass

class FooTyped(Typed):
    name = TypedProperty(str)
    num = TypedProperty(int, 43)


foo_typed = FooTyped()
foo_typed.name = "ales"
try:
    foo_typed.go = 'went'
except AttributeError as e:
    print(f"e={e}")



