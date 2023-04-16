import matplotlib.pyplot as plot
import numpy as np
xData = np.random.random_integers(18, 50, 50)
yData = np.random.random_integers(200, 800, 50)
plot.scatter(xData, yData)
plot.title('Hypothetical:Student age group and GMAT Score')
plot.xlabel('Age')
plot.ylabel('Score')
plot.show()