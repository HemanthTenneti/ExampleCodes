# Calculate and/or Manipulate Series object values
from pandas import Series
from numpy import array as arr, NaN, float32

section = ["12A", "12B", "12C", "12D", "12E"]
contribution = arr([5500, 7500, 9000, 3000, NaN])
classContrib = Series(contribution * 2, section, dtype=float32)
print(classContrib)
