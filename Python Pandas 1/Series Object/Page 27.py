##
# ! Example 20

# ! Series object s11 stores the charity contribution made by each section (see below):
# ? ---------------------
# ? |   A   |   6700    |
# ? |   B   |   5600    |
# ? |   C   |   5000    |
# ? |   D   |   5200    |
# ? ---------------------

# ! Write a program to display which sections made a contribution more than ₹5500/-

import pandas as pd

# ? Defining data for the s11 Series object
data = {"A": 6700, "B": 5600, "C": 5000, "D": 5200}
s11 = pd.Series(data)

# ? Printing contributions greater than 5500
print("Contribution > 5500 by :")
print(s11[s11 > 5500])
