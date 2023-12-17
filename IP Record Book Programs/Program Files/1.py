# Create a series object using a dictionary
from pandas import Series

studentDictionary = {"12A": 25, "12B": 27, "12C": 28, "12D": 23}
studentSeries = Series(studentDictionary)
print(studentSeries)
