# Program to modify elements of series object using index
from pandas import Series

section = ["12A", "12B", "12C", "12D", "12E"]
strength = [20, 25, 30, 25, 30]
ClassSer = Series(strength, section)
print(f"{ClassSer}\n" + "-" * 25)
print("Modifying elements of series:")
print("Using index:\nClassSer[0] = 40")
ClassSer[0] = 40
print(f"{ClassSer}\n" + "-" * 25)
print("Using start & stop:\nClassSer[2:4] = 50")
ClassSer[2:4] = 50
print(f"{ClassSer}\n" + "-" * 25)
print("Using start:\nClassSer[2:] = 100")
ClassSer[2:] = 100
print(f"{ClassSer}\n" + "-" * 25)
