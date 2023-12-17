# Program to create a dataframe of survey data with population, hospitals and schools
from pandas import DataFrame

survey = {
    "Population": {"Delhi": 3000, "Mumbai": 5000, "Kolkata": 4000, "Chennai": "2000"},
    "Hospitals": {"Delhi": 300, "Mumbai": 500, "Kolkata": 400, "Chennai": "200"},
    "Schools": {"Delhi": 30, "Mumbai": 50, "Kolkata": 40, "Chennai": "20"},
}
surveyDF = DataFrame(survey)
print(surveyDF)
print("-" * 45)

# A - Selecting / Accessing a column
print(surveyDF.Population)
print("-" * 45)
print(surveyDF["Population"])
print("-" * 45)

# B - Selecting / Accessing multiple columns
print(surveyDF[["Population", "Schools"]])
print("-" * 45)
print(surveyDF.Population, "\n", surveyDF.Schools)
print("-" * 45)

# C - Selecting / Accessing a subset from a DataFrame using row/column names
# i. To access a row
print(surveyDF.loc["Chennai", :])
print("-" * 45)

# ii. To access multiple rows
print(surveyDF.loc["Chennai":"Delhi", :])
print("-" * 45)

# D - To access selective columns
# i. All columns between start and end are listed
print(surveyDF.loc[:, "Population":"Schools"])
print("-" * 45)
# ii. Columns you want to fetch
print(surveyDF.loc[:, "Population":"Hospitals"])
print("-" * 45)

# E - To access range of columns from a range of rows
print(surveyDF.loc["Chennai":"Delhi", "Population":"Hospitals"])
print("-" * 45)

# F - Selecting rows/columns from DataFrame using index
print(surveyDF.iloc[0:2, 1:2])
print("-" * 45)
print(surveyDF.iloc[1:4, 1:3])
print("-" * 45)

# G - Selecting/Accessing Individual Value
# i. Column name/index
print(surveyDF.Population["Delhi"])
print("-" * 45)
# ii. at or iat
print(surveyDF.at["Chennai", "Population"])
print("-" * 45)

# H - Adding/Modifying Rows /Columns values in DataFrames
# i. With a single value
surveyDF["Hotels"] = 100
print(surveyDF)
print("-" * 45)
# ii. With a list
surveyDF["Hotels"] = [100, 200, 300, 400]
print(surveyDF)
print("-" * 45)
