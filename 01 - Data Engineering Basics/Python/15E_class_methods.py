class Animal:
    lEgs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} lEgs...'.format(name,cls.lEgs))
Animal.walk('Dog')
Animal.walk('Cat')