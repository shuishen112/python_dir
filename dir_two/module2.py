import sys
from os import path

# print(path.abspath(__file__))
# print(path.dirname(path.abspath(__file__)))
# print(path.dirname(path.dirname(path.abspath(__file__))))
# sys.path.append(".")
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from dir_one.module1 import my_print


my_print()
