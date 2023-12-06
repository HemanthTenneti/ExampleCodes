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

RollNo = [1, 2, 3, 4, 5]
Name = [
    "Prema Singh",
    "Manish Arora",
    "Tanish Goel",
    "Falguni Jain",
    "Kanika Bharatnagar",
]

UT1 = [24, 18, 20, 22, 15]
UT2 = [24, 17, 22, 20, 20]
UT3 = [20, 19, 18, 24, 18]
UT4 = [22, 22, 24, 20, 22]
data = {"RollNo": RollNo, "Name": Name, "UT1": UT1, "UT2": UT2, "UT3": UT3, "UT4": UT4}

printLines("Creating Dataframe")
df = pd.DataFrame(data)
print(df)

printLines("Displaying top 2 rows")
print(df.head(2))

printLines("Displaying the last 2 rows")
print(df.tail(2))

printLines("Adding column total")
df["Total"] = df["UT1"] + df["UT2"] + df["UT3"] + df["UT4"]
print(df)

printLines("Displaying the row having roll no. 4")
print(df[df["RollNo"] == 4])

printLines("Displaying column labels")
print(df.columns)

# ! MatPlotLib
import matplotlib.pyplot as plt

group = ["VII", "VIII", "IX", "X"]
noStudents = [40, 45, 35, 45]
plt.bar(group, noStudents)
plt.xlabel("Class")
plt.ylabel("Students")
plt.title("No of students in class")
plt.show()

# ! MySQL
# ? create table student(student_id int primary key, name varchar(255), marks decimal(10,2));
# ? insert into students values(125, 'Anitha', 98.15);
# ? delete from student;
# ? select * from student where marks > 80;
# ? select upper(name), lower(name), left(name, 3), right(name, 3) from student;
# ? select ltrim("Informatics Practices Class XII"), rtrim("Informatics Practices Class XII"), trim("Informatics Practices Class XII");
# ? select dayname(curdate()), monthname(curdate()), day(curdate()), datofmonth(curdate()), dayofyear(curdate());
