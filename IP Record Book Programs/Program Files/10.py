# Program to create a DataFrame of student data with age, section and location and perform

from pandas import DataFrame

student = {
    "Akash": {"Age": 15, "Section": "12A", "Loc": "Hyderabad", "Marks": 90},
    "Vishal": {"Age": 16, "Section": "12B", "Loc": "Bangalore", "Marks": 90},
    "Sameer": {"Age": 17, "Section": "12C", "Loc": "Delhi", "Marks": 90},
}
studentDF = DataFrame(student)
print(studentDF)
print("-" * 45)

# Modifying a single cell at once
studentDF.Akash["Section"] = "12D"
studentDF.Sameer["Loc"] = "Pune"
print(studentDF)

# Deleting rows/columns in a DataFrame
studentDF.drop(["Section"])
print(studentDF)
print("-" * 45)

# Renaming rows/columns
studentDF.rename(
    index={"Age": "A", "Loc": "L", "Marks": "M", "Section": "Sec"}, inplace=True
)
print(studentDF)
print("-" * 45)
