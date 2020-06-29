__all__ = ["some_number", "_some_protected_number"]

some_number = 13
_some_protected_number = 2.137e3


def func():
    print("Hello from func()")


def __private_func():
    print("Quite a special greeting from __private_func()")
