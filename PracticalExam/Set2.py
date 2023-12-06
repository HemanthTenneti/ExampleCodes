##
# ! Pandas
def printLines(a, b="sub heading"):
    if b.lower() == "title" or b.lower() == "t":
        print("-" * 80)
        print(f"{'-' * 20} {a}")
        print("-" * 80)
    else:
        print(f"{'-' * 10} {a}")


import pandas as pd
from os import name as OSNAME, system

system("clear" if OSNAME == "posix" else "cls")

printLines("Pandas", "t")

data = {
    "Maths": {"Amit": 100, "Mohan": 95, "Sudha": 85},
    "Science": {"Amit": 100, "Mohan": 50, "Sudha": 90},
    "SSt": {"Amit": 60, "Mohan": 57.48, "Sudha": 53.58},
}

printLines("Creating Database")
df = pd.DataFrame(data)
print(df)

printLines("Adding Column Total")
df["Total"] = df["Maths"] + df["Science"] + df["SSt"]
print(df)

printLines("Adding Column T5 with values")
df.loc["T5", :] = [75.6, 98.6, 56.6, 230.8]
print(df)

printLines("Printing Score of Maths and Sciences")
print(df[["Maths", "Science"]])

printLines("Updating Value of Sudha")
df.at["Sudha", "Science"] = 85.0
print(df)

printLines("Deleting a row")
df = df.drop("Mohan")
print(df)

# ! MatPlotLib
import matplotlib.pyplot as plt
import numpy as np

subjects = ["Maths", "Science", "SSt"]
Amit = [100, 100.0, 60.0]
Mohan = [95, 50, 57.48]
Sudha = [85, 100.0, 53.58]
x_axis = np.arange(len(subjects))
plt.bar(x_axis - 0.25, Amit, 0.25, label="Amit")
plt.bar(x_axis, Mohan, 0.25, label="Mohan")
plt.bar(x_axis + 0.25, Sudha, 0.25, label="Sudha")
plt.xticks(x_axis, subjects)
plt.legend(loc=1)
plt.xlabel("Name")
plt.ylabel("Score")
plt.title("Results")
plt.show()

# ! MySQL
# ? select item, unitprice from infant where unitprice < 800 and discount>5;
# ? select count(*) from infant where discount > 10;
# ? select itemcode, unitprice from infant order by unitprice desc;
# ? update infant set unitprice = unitprice+unitprice*10/100
# ? select max(unitprice) from infant;
