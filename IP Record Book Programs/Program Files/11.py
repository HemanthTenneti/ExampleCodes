# Program to plot a line chart to depict the changing weekly onion prices for four weeks. Give appropriate axes labels
from matplotlib.pyplot import plot, xlabel, ylabel, show

week = [1, 2, 3, 4]
prices = [40, 80, 100, 50]
plot(week, prices)
xlabel("Week")
ylabel("Onion Prices (Rs.)")
show()
