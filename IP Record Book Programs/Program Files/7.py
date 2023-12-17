# Program to sort series values based on values and indices
from pandas import Series

section = ["12A", "12B", "12C", "12D", "12E"]
strength = [20, 25, 30, 15, 30]
p = Series(strength, section)
print(f"Sorting values by ascending:\n{p.sort_values()}\n" + "-" * 40)
print(f"Sorting values by descending:\n{p.sort_values(ascending=False)}\n" + "-" * 40)
print(f"Sorting index by descending:\n{p.sort_index(ascending=False)}\n" + "-" * 40)
print(f"Sorting index by ascending:\n{p.sort_index(ascending=True)}\n" + "-" * 40)
