# Program to extract slices from series object
from pandas import Series

SNo = [0, 1, 2, 3, 4, 5, 6]
fruits = ["Apple", "Banana", "Grapes", "Jackfruit", "Mango", "Orange", "Pineapple"]
fruitSeries = Series(fruits, SNo)
print(fruitSeries)
print("-" * 30)
print(f"fruitSeries[1:] value:\n{fruitSeries[1:]}")
print("-" * 30)
print(f"fruitSeries[2:5] value:\n{fruitSeries[2:5]}")
print("-" * 30)
print(f"fruitSeries[0::2] value:\n{fruitSeries[0::2]}")
print("-" * 30)
print(f"fruitSeries[-3] value:\n{fruitSeries[-3:]}")
print("-" * 30)
print(f"fruitSeries[:-3] value:\n{fruitSeries[:-3]}")
print("-" * 30)
