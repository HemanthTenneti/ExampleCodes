##
#! -- 1. Pandas --
from pandas import DataFrame

# ? Creating DataFrame
print("Creating the DataFrame")

team1 = {"P1": [700, 975, 970, 900], "P2": [490, 460, 570, 590]}
team2 = {"P1": [1100, 1275, 1270, 1400], "P2": [1400, 1260, 1500, 1190]}
index = [1, 2, 3, 4]

df1 = DataFrame(team1, index)
df2 = DataFrame(team2, index)

print("DataFrame of Team 1:")
print(df1)
print()
print("DataFrame of Team 2:")
print(df2)
print()

# ? Calculating total points earned by both the teams
total = df1 + df2

print("DataFrame of Total Points:")
print(total)


#! -- 2. Matplotlib --
from matplotlib.pyplot import bar, xlabel, ylabel, title, show

years = [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018]
production = [4, 6, 7, 15, 24, 2, 19, 5, 16, 4]

bar(years, production, color="skyblue")
xlabel("Year")
ylabel("Production")
title("Wheat Production in Different Years")

show()


#! -- 3. MySQL --
# ? StudentNo     Class     Name        Game1        Grade1     Game2        Grade2
# ? 10            7         Sameer      Cricket      B          Swimming     A
# ? 11            8         Sujit       Tennis       A          Skating      C
# ? 12            7         Kamal       Swimming     B          Football     B
# ? 13            7         Veena       Tennis       C          Tennis       A
# ? 14            9         Archana     Basketball   A          Cricket      A
# ? 15            10        Arpit       Cricket      A          Athletics    C


# ? Creating the table and inserting values
# * create database Preboard;
# * use Preboard;
# * create table sports(
# * StudentNo int primary key,
# * Class int,
# * Name varchar(50),
# * Game1 varchar(50),
# * Grade1 varchar(1),
# * Game2 varchar(50),
# * Grade2 varchar(1)
# * );
# * insert into sports values
# * (10, 7, 'Sameer', 'Cricket', 'B', 'Swimming', 'A'),
# * (11, 8, 'Sujit', 'Tennis', 'A', 'Skating', 'C'),
# * (12, 7, 'Kamal', 'Swimming', 'B', 'Football', 'B'),
# * (13, 7, 'Veena', 'Tennis', 'C', 'Tennis', 'A'),
# * (14, 9, 'Archana', 'Basketball', 'A', 'Cricket', 'A'),
# * (15, 10, 'Arpit', 'Cricket', 'A', 'Athletics', 'C');
# * select * from sports;


# ? Display names of students who have grade "C" in either Game1 or Game2 or both
# * select Name from sports where grade1 = 'C' or grade2 = 'C';

# ? Concatenate Name and Game1 columns
# * select concat(Name, "-", Game1) from sports;

# ? Display the position of 'e' in the name column of sports
# * select Name, position('e' in Name) from sports;

# ? Display maximum StudentNo class-wise
# * select Class, max(StudentNo) from sports group by class;

# ? Display maximum StudentNo class wise whose StudentNo is more than 7
# * select Class, max(StudentNo) from sports where StudentNo > 7 group by Class;
