# Read from a CSV file and create a DataFrame from it but DataFrame should not use file’s column header. And also it should print the maximum, minimum salary given to an employee
from pandas import read_csv

csvRead = read_csv(
    r"Record Book Programs/Program Files/EmpData.csv",
    names=["EmpId", "EmpName", "EmpDesig", "EmpSal"],
    skiprows=1,
)
print(csvRead)
print("Maximum Salary is ", csvRead.EmpSal.max())
print("Minimum Salary is ", csvRead.EmpSal.min())
