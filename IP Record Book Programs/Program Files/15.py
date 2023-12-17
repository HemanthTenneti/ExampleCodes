# Program to read from a CSV file Employee.csv and create a dataframe from it.
from pandas import read_csv

csvRead = read_csv(r"Record Book Programs/Program Files/EmpData.csv")
print(csvRead)
