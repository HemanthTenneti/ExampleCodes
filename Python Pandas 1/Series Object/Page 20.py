##
# ! Example 14

# ! Consider a series object s8 that stores the number of students in each section of class 12.
# ? -------------------
# ? |   A   |   39    |
# ? |   B   |   41    |
# ? |   C   |   42    |
# ? |   D   |   44    |
# ? -------------------
# ! First two sections have been given a task of selling tickets @ 100/- per ticket as part of a social experiment.
# ! Write a code to display how much they have collected.


import pandas as pd

# ? Defining data in a dictionary for the Series object
stu = {"A": 39, "B": 41, "C": 42, "D": 44}
s8 = pd.Series(stu)
# ? Printing the tickets amount
print("Tickets Amount")
print(s8[:2] * 100)
