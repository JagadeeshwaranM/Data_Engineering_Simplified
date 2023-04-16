import matplotlib.pyplot as plot
years = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2017]
indexValues = [68, 81, 71, 244, 151, 200, 615, 809, 824, 2633, 10787, 11577, 20656]
plot.grid(True, which="both")
plot.semilogy(years, indexValues)
plot.ylim([10, 21000])
plot.xlim([1900, 2020])
plot.title('Y axis in Semilog using Python Matplotlib')
plot.xlabel('Year')
plot.ylabel('Stock market index')
plot.show()