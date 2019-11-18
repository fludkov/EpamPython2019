# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка
перестановкой другой. Под перестановкой понимаем любое
изменение порядка символов. Регистр учитывается, пробелы
являются существенными.
"""


def is_permutation(a: str, b: str) -> bool:
    """This function accepts on entry two string values and returns
    a boolean value if 'a' string is permutation of 'b' string"""

    return True if sorted(a) == sorted(b) else False

    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками

assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')
