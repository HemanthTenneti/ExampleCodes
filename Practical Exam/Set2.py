##
#! -- 1. Pandas --
from pandas import DataFrame

# ? Creating DataFrame
print("Creating the DataFrame")

data = {
    "TV": [200000, 230000, 210000, 240000],
    "FRIDGE": [300000, 200000, 290000, 210000],
    "AC": [240000, 153000, 245000, 170000],
}
index = ["QTR1", "QTR2", "QTR3", "QTR4"]

df = DataFrame(data, index=index)

print(df)


#! -- 2. Matplotlib --
from matplotlib.pyplot import plot, xlabel, ylabel, plot, legend, grid, show, title

years = [1960, 1970, 1980, 1990, 2000, 2010]
pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]

plot(years, pakistan, label="Population of Pakistan")
plot(years, india, label="Population of India")
xlabel("Year")
ylabel("Population (in millions)")
title("Population of India and Pakistan Over the Years")
legend()

grid(True)
show()


#! -- 3. MySQL --
# ? PNo     Name        Age     Department           Dateofadm       Charges     Gender
# ? 1       Arprit      62      Surgery              2008-01-12      300         M
# ? 2       Zarina      22      ENT                  2007-12-12      250         F
# ? 3       Kareem      32      Orthopaedic          2008-02-19      200         M
# ? 4       Arun        12      Surgery              2008-01-11      300         M
# ? 5       Zubin       30      ENT                  2008-01-12      250         M
# ? 6       Ketaki      16      ENT                  2008-02-24      250         M
# ? 7       Ankita      29      Cardiology           2008-02-20      800         F
# ? 8       Zareen      45      Gynaecology          2008-02-22      300         F
# ? 9       Kush        19      Cardiology           2008-01-13      800         M
# ? 10      Shilpa      23      Nuclear Medicine     2008-01-20      400         F

# ? Creating the table and inserting values
# * create database Preboard;
# * use Preboard;
# * create table hospital(
# * PNo int primary key,
# * Name varchar(50),
# * Age int,
# * Department varchar(50),
# * Dateofadm date,
# * Charges int,
# * Gender varchar(1)
# * );
# * insert into hospital values
# * (1, 'Arprit', 62, 'Surgery', '2008-01-12', 300, 'M'),
# * (2, 'Zarina', 22, 'ENT', '2007-12-12', 250, 'F'),
# * (3, 'Kareem', 32, 'Orthopaedic', '2008-02-19', 200, 'M'),
# * (4, 'Arun', 12, 'Surgery', '2008-01-11', 300, 'M'),
# * (5, 'Zubin', 30, 'ENT', '2008-01-12', 250, 'M'),
# * (6, 'Ketaki', 16, 'ENT', '2008-02-24', 250, 'M'),
# * (7, 'Ankita', 29, 'Cardiology', '2008-02-20', 800, 'F'),
# * (8, 'Zareen', 45, 'Gynaecology', '2008-02-22', 300, 'F'),
# * (9, 'Kush', 19, 'Cardiology', '2008-01-13', 800, 'M'),
# * (10, 'Shilpa', 23, 'Nuclear Medicine', '2008-01-20', 400, 'F');
# * select * from hospital;

# ? List names of patients in ascending order of date of admission
# * select Name, Dateofadm from hospital order by Dateofadm asc;

# ? Display department-wise total charges whose maximum charges more than or equal to 300
# * select Department, sum(Charges) from hospital group by department having max(Charges) >= 300;

# ? Display the position of 'a' in the name column
# * select Name, position('a' in Name) from hospital;

# ? Display the 3 characters from 1st position of department column
# * select Department, mid(Department, 1, 3) from hospital;

# ? Display gender-wise total charges
# * select Gender, sum(Charges) from hospital group by Gender;
