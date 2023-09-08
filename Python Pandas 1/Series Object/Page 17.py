##
# ! Example 13

# ! Consider the two series objects s11 and s112 that you created in examples 11 nd 12 respectively. Print the attributes of both these objects in a report form as shown below:
# ? ----------------------------------------------------------
# ? | Attribute Name    |   Object s11    |     Object s12   |
# ? |--------------------------------------------------------|
# ? | Data type         |                 |                  |
# ? | Shape             |                 |                  |
# ? | No. of bytes      |                 |                  |
# ? | No. of dimensions |                 |                  |
# ? | Item size         |                 |                  |
# ? | Has NaNs ?        |                 |                  |
# ? | Empty ?           |                 |                  |
# ? ----------------------------------------------------------

import pandas as pd
import numpy as np

# ? Defining data for the Series object
section = ["A", "B", "C", "D"]
contri = [6700, 5600, 5000, 5200]

# ? Creating Series object with the pre-defined data
s11 = pd.Series(data=contri, index=section)

# ? Defining data for the Series object pre-defined data

section1 = ["A", "B", "C", "D", "E"]
contri1 = np.array([6700, 5600, 5000, 5200, np.NaN])
# ? Creating Series object with
s12 = pd.Series(data=contri1 * 2, index=section1, dtype=np.float32)

# ? Printing all different attributes of the Series objects s11, and s12
print(f"{'Attribute name':<30}    {'Object s11':<15}{'Object s12'}")
print(f"{'Data type (.dtype)':<30}:   {f'{s11.dtype}' :<15}{s12.dtype}")
print(f"{'Shape (.shape)':<30}:   {f'{s11.shape}':<15}{s12.shape}")
print(f"{'No. of bytes (.nbytes)':<30}:   {f'{s11.nbytes}':<15}{s12.nbytes}")
print(f"{'No. of dimensions (.ndim)':<30}:   {f'{s11.ndim}':<15}{s12.ndim}")
print(
    f"{'Item size (.itemsize)':<30}:   {f'{s11.values.itemsize}':<15}{s12.values.itemsize}"
)
print(f"{'Has NaNs? (.hasnans)':<30}:   {f'{s11.hasnans}':<15}{s12.hasnans}")
print(f"{'Empty? (.empty)':<30}:   {f'{s11.empty}':<15}{s12.empty}")
