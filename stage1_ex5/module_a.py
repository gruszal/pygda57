import sys
sys.path.append('b.zip')
print(sys.path)

from b.module_b1 import func_b1

func_b1()