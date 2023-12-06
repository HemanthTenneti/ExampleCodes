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


printLines("Pandas", "t")

printLines("Creating Database")
serObj = pd.Series([31, 28, 31, 30], index=["Jan", "Feb", "Mar", "Apr"])
print(serObj)

printLines("Adding May")
serObj["May"] = 31
print(serObj)

printLines("Updating Feb")
serObj["Feb"] = 29
print(serObj)

printLines("Replacing Index")
serObj.index = [1, 2, 3, 4, 5]
print(serObj)

printLines("Printing month having less than 31 days")
print([serObj < 31].index)

printLines("V (a)")
print(serObj < 30)

printLines("V (b)")
print(serObj + 3)


# ! MatPlotLib
import matplotlib.pyplot as plt

group = ["I", "II", "III", "IV"]
strength = [38, 30, 45, 49]

plt.bar(group, strength, color=["red", "green", "blue", "black"])
plt.xlabel("Group")
plt.ylabel("Strength")
plt.title("Group-wise Strength")
plt.grid(True)
plt.show()


# ! MySQL
# ? update drugdb set price = price+35 where drugname = 'Paracetamol';
# ? select drugid, rxid, pharmacyName from drugdb order by price desc;
# ? select * from drugdb where drugname like 'C%SH%';
# ? select lower(drugname), round(price, 0) from drugdb;
# ? alter table drugdb drop loc;
