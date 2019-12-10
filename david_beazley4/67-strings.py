#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 67
Строки
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"

s = "операции, общие для, всех типов, последовательностей \t\tEND"
print(f"s.capitalize()={s.capitalize()}")
print(f"s.expandtabs()={s.expandtabs()}")
print(f"s.center()={s.center(100)}")
snums = "3452094"
print(f"s.isalnum()={s.isalnum()}")
print(f"snums.isalnums()={snums.isalnum()}")
print(f"snums.isupper()={snums.isupper()}")
supper = "GOGOGOG"
print(f"supper.isupper()={supper.isupper()}")
print(f"s.sprit(',')={s.split(',')}")
print(f"s.rsprit(',')={s.rsplit(',')}")
print(f"s.partition(',')={s.partition(',')}")
print(f"s.rpartition(',')={s.rpartition(',')}")
#print(f"s.find('о', start=3)={s.find('о', start=3)}")
#transtab = zip("орц", "357")
#print(f"s.translate(transtab)={s.translate('о1р2ц3')}")
print(f"s.encode()={s.encode()}")
print(f"s.encode()={s.encode().decode()}")
print(f"s.endswith('END')={s.endswith('END')}")
print(f"s.startswith('END')={s.startswith('START')}")
print(f"s.isalpha()={s.isalpha()}")
print(f"s.islower()={s.islower()}")
print(f"s.isspace()={s.isspace()}")  # Проверяет, являются ли все символы в строке пробельными символами.
print(f"s.istitle()={s.istitle()}")  # Проверяет, являются ли первые символывсех слов символами верхнего регистра.
print(f"s.lstrip()={s.lstrip('еоп')}")  # Выравнивает строку s по левому краю в поле шириной width
print(f"s.rjust()={s.rjust(100)}")

sm = """Преобразует строку в список строк. Если
аргумент keepnds имеет значение 1, завер-
шающие символы перевода строки остаются
нетронутыми.
"""
print(sm.splitlines(keepends=True))
print(f"s.swapcase()={s.swapcase()}")
print(f"s.title()={s.title()}")
print(f"s.zfill()={s.zfill(100)}")
