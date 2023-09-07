##
# ! --> Example 6
import pandas as pd
import numpy as np  # * ERROR: Forgot to import numpy in the textbook example.

# ? Creating a Series object with data made by a numpy library
s6 = pd.Series(np.linspace(24, 64, 5))
# ? Printing Series object
print(s6)


# ! --> Example 7
import pandas as pd
import numpy as np  # * ERROR: Forgot to import numpy in the textbook example.

# ? Creating a Series object with data made by a numpy library
s7 = pd.Series(np.tile([3, 5], 2))
# ? Printing Series object
print(s7)


# ! --> Example 8
import pandas as pd

# ? Defining data for the Series object
stu = {"A": 39, "B": 41, "C": 42, "D": 44}
# ? Creating a Series object using dictionary as data input
s8 = pd.Series(stu)

# ? Printing Series object
print(s8)
