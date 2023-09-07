##
# ! Example 12

import pandas as pd
import numpy as np

# ? Defining data for the Series object
section = ["A", "B", "C", "D", "E"]
contri1 = np.array([6700, 5600, 5000, 5200, np.NaN])
# ? Creating Series object with defined values
s12 = pd.Series(data=contri1 * 2, index=section, dtype=np.float32)
# ? Printing Series object
print(s12)
