##
# ! Example 19

# ! What will be the output produced by the following program
# ? import pandas as pd
# ? info = pd.Series(data=[31,41,51])
# ? print(info)
# ? print(info > 40)
# ? print(info[info > 40])

# ? Answer:
# * -> 0 31
# * -> 1 41
# * -> 2 51
# * -> dtype: int64
# * -> 0 False
# * -> 1 True
# * -> 2 True
# * -> dtype: bool
# * -> 1 41
# * -> 2 51
# * -> dtype: int64
