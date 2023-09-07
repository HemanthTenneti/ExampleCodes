##
# ! --> Example 9
import pandas as pd

# ? Creating a Series object with same value (5000) but different provided indices
s9 = pd.Series(5000, index=["Qtr1", "Qtr2", "Qtr3", "Qtr4"])
# ? Printing Series object
print(s9)


# ! --> Example 10
import pandas as pd

# ? Creating a Series object with same value (200) but different indices using range function
s10 = pd.Series(200, index=range(2020, 2029, 2))
# ? Printing Series Object
print(s10)
