##
# ! Pandas
import pandas as pd
import numpy as np

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

df = pd.DataFrame(data)
print(df)
print(df.head(2))
print(df.tail(2))
print(UT1 + UT2 + UT3 + UT4)
df["Total"] = df["UT1"] + df["UT2"] + df["UT3"] + df["UT4"]
print(df)
print(df[df["RollNo"] == 4])
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
