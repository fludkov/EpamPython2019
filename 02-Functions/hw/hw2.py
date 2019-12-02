from collections import namedtuple
def atom(x=None):

    Functions = namedtuple("Functions", "get_value set_value process_value delete_value")

    def get_value():
        return x
    def set_value(y):
        nonlocal x
        x=y
        return x
    def process_value(*funcs):
        for func in funcs:
            x=func(x)
    def delete_value():
        nonlocal x
        del x
    return Functions("Functions", [get_value, set_value, process_value, delete_value])


a = atom(1)
print(a.get_value())