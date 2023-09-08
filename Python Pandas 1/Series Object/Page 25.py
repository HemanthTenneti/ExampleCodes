##
# ! Example 17

# ! Number of students in classes 11 and 12 in three streams ('Science', 'Commerce' and 'Humanities') are stored in two Series objects c11 and 12. Write code to find total number of students in classes 11 and 12, stream wise.

import pandas as pd

# ? Creating Series object for each stream
c11 = pd.Series(data=[30, 40, 50], index=["Science", "Commerce", "Humanities"])
c12 = pd.Series(data=[37, 44, 45], index=["Science", "Commerce", "Humanities"])

# ? Printing total number of students in the streams
print("Total no. of students")
print(c11 + c12)

# ! Example 18

# ! Object1 Population stores the details of population in four metro cities of India and Object2 AvgIncome stores the total average income reported in previous year in each of these metros. Calculate income per capita for each of these metro cities.

import pandas as pd

# ? Creating Series objects for each attribute, i.e., Population, Income, perCapita
Population = pd.Series(
    [10927986, 12691836, 4631392, 4328063],
    index=["Delhi", "Mumbai", "Kolkata", "Chennai"],
)
AvgIncome = pd.Series(
    [72167810927986, 85087812691836, 4226784631392, 5261784328063],
    index=["Delhi", "Mumbai", "Kolkata", "Chennai"],
)
perCapita = AvgIncome / Population

# ? Printing the Series objects
print("Population in four metro cities ")
print(Population)
print("Avg. Income in four metro cities")
print(AvgIncome)
print("Per Capita Income in four metro cities ")
print(perCapita)
