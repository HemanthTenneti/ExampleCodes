# Program to demonstrate dataframe attributes / properties
from pandas import DataFrame
from numpy import NaN

peopleData = DataFrame(
    {
        "Weight": [20, 36, NaN],
        "Name": ["Nihal", "Sameera", "Ajay"],
        "Gender": ["Male", "Female", "Male"],
    }
)
print(f"Original DataFrame:\n{peopleData}\n" + "-" * 40)
print(f"Index:\n{peopleData.index}\n" + "-" * 40)
print(f"Column:\n{peopleData.columns}\n" + "-" * 40)
print(f"Axes:\n{peopleData.axes}\n" + "-" * 40)
print(f"d-Types:\n{peopleData.dtypes}\n" + "-" * 40)
print(f"Size:\n{peopleData.size}\n" + "-" * 40)
print(f"Shape:\n{peopleData.shape}\n" + "-" * 40)
print(f"Values:\n{peopleData.values}\n" + "-" * 40)
print(f"IsEmpty:\n{peopleData.empty}\n" + "-" * 40)
print(f"n-Dimensions:\n{peopleData.ndim}\n" + "-" * 40)
print(f"Transpose:\n{peopleData.T}\n" + "-" * 40)
