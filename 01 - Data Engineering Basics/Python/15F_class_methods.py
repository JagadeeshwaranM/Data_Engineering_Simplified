class TestMath:
    @staticmethod
    def add(x,y):
        print('The Sum:',x+y)
    @staticmethod
    def product(x,y):
        print('The Product:',x*y)
    @staticmethod
    def average(x,y):
        print('The average:',(x+y)/2)
TestMath.add(10,20)
TestMath.product(10,20)
TestMath.average(10,20)