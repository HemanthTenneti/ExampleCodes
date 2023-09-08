##
# ! Example 16

# ! A series object trdata consists of around 2500 rows of data. Write a program to print the following details:
# ! (i) First 100 rows of data       (ii) Last 5 rows of data

import pandas as pd
import random

# ? Generating random values for trdata object here
data = []
for i in range(2500):
    data.append(random.randint(0, 10000))
trdata = pd.Series(data)

# ? Printing the (i) & (ii) values
print(trdata.head(100))
print(trdata.tail())
