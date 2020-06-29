print(__file__)
print(f"\tname: {__name__}, package: {__package__}\n")

from .module_b2 import func_b2


def func_b1():
    print("Hello from func_b1()")


func_b2()
