##
#! -- 1. Pandas --
from pandas import Series

# ? Creating Series
print("Creating the Series")

S = Series({"A": 4300, "B": 6500, "C": 3900, "D": 6100})

print(S)
print()

# ? Modifying
print("Modifying the Series")

S["A"] = 3400
S["C"] = S["D"] = 5000

print(S)


#! -- 2. Matplotlib --
from matplotlib.pyplot import plot, title, xlabel, ylabel, show, legend

names = ["Ram", "Shyam", "Rama", "Kashish", "Mayank"]
accountancy = [87, 82, 99, 85, 80]
bst = [90, 79, 95, 93, 85]

plot(names, accountancy, label="Accountancy")
plot(names, bst, label="Business Studies")

title("Student Data Analysis")
xlabel("Students")
ylabel("Scores")
legend()

show()


#! -- 3. MySQL --
# ? No      Name             Price           Supplier           Stock
# ? 1       Motherboard      7000            Intel              20
# ? 2       Keyboard         1000            TVSE               70
# ? 3       Mouse             500            Logitech           20
# ? 4       Soundcard         600            Samsung            20
# ? 5       Speaker           600            Samsung            20
# ? 6       Monitor          3000            Philips            20
# ? 7       CD-ROM           2800            Creative           20
# ? 8       Printer          7900            HP                 20

# ? Creating the table and inserting values
# * create database HusainPreboard;
# * use HusainPreboard;
# * create table product(
# * No int primary key,
# * Name varchar(50),
# * Price int,
# * Supplier varchar(50),
# * Stock int
# * );
# * insert into product values
# * (1, "Motherboard", 7000, "Intel", 20),
# * (2, "Keyboard", 1000, "TVSE", 70),
# * (3, "Mouse", 500, "Logitceh", 60),
# * (4, "Soundcard", 600, "Samsung", 50),
# * (5, "Speakers", 600, "Samsung", 25),
# * (6, "Monitor", 3000, "Philips", 22),
# * (7, "CD-ROM", 2800, "Creative", 32),
# * (8, "Printer", 7900, "HP", 10);
# * select * from product;

# ? Display name and price in descending order of stock
# * select name,price from product order by stock desc;

# ? Display position of 'a' in name column
# * select name, position('a' in name) from product;

# ? Display 3 characters from 2nd position of supplier column
# * select supplier, mid(supplier, 2, 3) from product;

# ? Display average price of each supplier
# * select supplier, avg(price) from product group by supplier;

# ? Display average price of each supper whose supplier is 'Samsung'
# * select supplier, avg(price) from product where supplier="Samsung" group by supplier;
