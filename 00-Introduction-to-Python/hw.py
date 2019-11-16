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
    a_list = list(a)
    b_list = list(b)
    for i in a:
        if i in b_list:
            a_list.remove(i)
            b_list.remove(i)
        else:
            return False
    if a_list == b_list:
        return True
    else:
        return False
    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками


assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')
