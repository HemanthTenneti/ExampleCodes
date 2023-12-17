# Program to plot a bar chart from the medals won by Australia. In the same chart, plot medals won by India too, based on the table given below
# Country    Gold   Silver   Bronze   Total
# Australia   80      59       59      198
# India       26      20       20      66
from matplotlib.pyplot import bar, xlabel, ylabel, show, title

MedalTypes = ["Gold", "Silver", "Bronze", "Total"]
Australia = [80, 59, 59, 198]
India = [26, 20, 20, 66]
bar(MedalTypes, Australia)
bar(MedalTypes, India)
title("Australia v. India Medal Count Comparison")
xlabel("Medal type")
ylabel("Medals won")
show()
