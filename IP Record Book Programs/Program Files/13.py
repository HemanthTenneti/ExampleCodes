# Program to plot a bar chart from the medals won by top four countries. Give appropriate axes labels, chart title and legend. Make sure that bars are separately visible
# Country    Gold   Silver   Bronze   Total
# Australia   80      59       59      198
# England     45      45       46      136
# India       26      20       20      66
# Canada      15      40       27      82

from matplotlib.pyplot import figure, bar, xlabel, ylabel, show, title
from numpy import arange

figure(figsize=(10, 7))
MedalTypes = ["Gold", "Silver", "Bronze", "Total"]
Australia = [80, 59, 59, 198]
England = [45, 45, 46, 136]
India = [26, 20, 20, 66]
Canada = [15, 40, 27, 82]
X = arange(len(MedalTypes))
bar(MedalTypes, Australia, width=0.15)
bar(X + 0.15, England, width=0.15)
bar(X + 0.30, India, width=0.15)
bar(X + 0.45, Canada, width=0.15)
xlabel("Medal type")
ylabel("Medals won")
title("Top Four Country's tally")
show()
