print(__file__)
print(f"\tname: {__name__}, package: {__package__}\n")

# __package__ = 'x.c'  # uncomment me!

from ..has_func import func

func()
