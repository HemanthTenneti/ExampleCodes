##
# ! --> Example 11
import pandas as pd

# ? Defining data for the Series object
section = ["A", "B", "C", "D"]
contri = [6700, 5600, 5000, 5200]

# ? Creating Series object with the d
s11 = pd.Series(data=contri, index=section)
# ? Printing Series object
print(s11)
