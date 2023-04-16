import numpy as np
import matplotlib.pyplot as plotter
numberOfYears = 5
averageReturns = (13, 15, 15, 14, 12)
categories = ('2012', '2013', '2014', '2015', '2016')
barWidth = 0.4
barOpacity = 0.5
barChart = plotter.bar(categories,averageReturns,barWidth,
                       alpha=barOpacity,
                       color='blue',
                       label=' Stock Returns')
plotter.xlabel('Year')
plotter.ylabel('Average returns from Stock Market %')
plotter.title('Annual Stock Market Returns %')
plotter.xticks(categories)
plotter.legend()
plotter.tight_layout()
plotter.show()