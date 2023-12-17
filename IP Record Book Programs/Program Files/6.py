# Program to demonstrate head and tail functions
from pandas import Series

ser = Series(["a", "b", "c", "d", "e", "f", "g", "h"])
print(f"head(5):\n{ser.head(5)}\n" + "-" * 25)
print(f"tail():\n{ser.tail()}\n" + "-" * 25)
print(f"head(2):\n{ser.head(2)}\n" + "-" * 25)
