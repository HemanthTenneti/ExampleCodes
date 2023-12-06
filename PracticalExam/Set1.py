##
# ! Pandas

import pandas as pd

serObj = pd.Series([31, 28, 31, 30], index=["Jan", "Feb", "Mar", "Apr"])
print(serObj)
serObj["Feb"] = 29
print(serObj)
serObj.index = [1, 2, 3, 4]
print(serObj)
print([serObj < 31].index)


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
