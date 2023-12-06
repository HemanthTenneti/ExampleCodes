##
# ! Pandas
import pandas as pd

BNo = [1, 2, 3, 4]
Name = ["Sunil Pillai", "Gaurav Sharma", "Piyush Goel", "Karthik Thakur"]
Score1 = [90, 65, 70, 80]
Score2 = [80, 45, 90, 76]
data = {"BNo": BNo, "Name": Name, "Score1": Score1, "Score2": Score2}

batsman = pd.DataFrame(data)
print(batsman)
batsman["Total"] = batsman["Score1"] + batsman["Score2"]
print(batsman)
print(f"Highest of Score2 = {batsman['Score2'].max()}")
print(batsman)
print(batsman[batsman["Name"] == "Piyush Goel"])

# ! MatPlotLib
import matplotlib.pyplot as plt

Grp = [1, 2, 3]
noStudents = [40, 50, 10]
plt.plot(Grp, noStudents)
plt.grid(True)
plt.xlabel("Class")
plt.ylabel("Student")
plt.title("Number of Students in Class")
plt.show()

# ! MySQL
# ? select carname from carden where color='Silver';
# ? select carname, company, capacity from carden order by capacity desc;
# ? select max(changes) from carden;
# ? update carden set charges = charges*1.05 where company='suzuki';
# ? select carname, company from carden where carname like '%n%' or charges>14;
