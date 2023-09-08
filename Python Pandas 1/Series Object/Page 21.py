##
# ! Example 15

# ! Consider a series object s13 that stores the number of students in each section of class 12.
# ? -------------------
# ? |   A   |  6700   |
# ? |   B   |  5600   |
# ? |   C   |  5000   |
# ? |   D   |  5200   |
# ? -------------------
# ! Write code to modify the amount of section 'A' as 7600 and for sections 'C' and 'D' as 7000. Print the changed object.

import pandas as pd

# ? Defining data in a dictionary
data = {"A": 6700, "B": 5600, "C": 5000, "D": 5200}
s13 = pd.Series(data)

s13[0] = 7600
s13[2:] = 7000
print("Series object after modifying amounts: ")
print(s13)
