import matplotlib.pyplot as plotter
sectors_label = 'Finance', 'Technology', 'Oil&Gas', 'BasicMaterial', 'Industrials', 'ConsumerGoods','Healthcare','ConsumerService','Others'
sectors_percent = [20.00, 11.5, 19.5, 7.25, 18.75, 6.75,6.75,9.25,0.25]
figureObject, axesObject = plotter.subplots()
explodeTuple = (0.0, 0.0, 0.1, 0.0, 0.0, 0.0,0.0,0.0,0.0)
axesObject.pie(sectors_percent,explode=explodeTuple,
               labels=sectors_label,
               autopct='%1.2f',
               startangle=90)
axesObject.axis('equal')
plotter.show()
