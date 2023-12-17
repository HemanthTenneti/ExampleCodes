# Ajay is doing research work in the field of Environment. For some plotting purpose he has generated some data as:
# mu=100
# sigma=15
# x=mu+sigma*np.random.randn(10000)
# y=mu+30*np.random.randn(10000)
# Plot the data on a bar stacked horizontal histogram with both x and y
from numpy.random import randn
from matplotlib.pyplot import hist, title, show

mu = 100
sigma = 15
x = mu + sigma * randn(10000)
y = mu + 30 * randn(10000)
hist([x, y], bins=100, histtype="barstacked")
title("Research data histogram")
show()
