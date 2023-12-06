##
# ! Pandas
import pandas as pd
import numpy as np

data = {
    "Col1": {"T1": 50, "T2": 95.5, "T3": np.NaN, "T4": 82.0},
    "Col2": {"T1": 98.0, "T2": 65.0, "T3": 75.0, "T4": 85.5},
    "Col3": {"T1": 60.0, "T2": 57.5, "T3": 69.5, "T4": 49.0},
}

result = pd.DataFrame(data)
print(result)
result["Total"] = result["Col1"] + result["Col2"] + result["Col3"]
print(result)
result.loc["T5", :] = [75.5, 98.0, 56.0, 229.5]
print(result)
result.rename(columns={"Col1": "Maths", "Col2": "Science", "Col3": "Social"})
print(result)
# print(result[["Maths", "Science"]])
result.at["T3", "Maths"] = 85.0
print(result)

# ! MatPlotLib
import matplotlib.pyplot as plt
import numpy as np

subjects = ["Maths", "Science", "SSt"]
Amit = [100, 100.0, 60.0]
Mohan = [95, 50, 57.48]
Sudha = [85, 100.0, 53.58]
xaxis = [1, 2, 3]
plt.plot(xaxis, Amit, label="Amit")
plt.plot(xaxis, Mohan, label="Mohan")
plt.plot(xaxis, Sudha, label="Sudha")
plt.xticks(xaxis, subjects)
plt.legend(loc=1)
plt.xlabel("Subjects Name")
plt.ylabel("Score")
plt.title("Result Analysis")
plt.show()

# ! MySQL
# ? select carname from carden where color='Silver';
# ? select carname, company, capacity from carden order by capacity desc;
# ? select max(changes) from carden;
# ? update carden set charges = charges*1.05 where company='suzuki';
# ? select carname, company from carden where carname like '%n%' or charges>14;
