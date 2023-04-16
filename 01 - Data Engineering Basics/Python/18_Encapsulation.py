#Encapsulation
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Employee(Person):
    all_employees = []
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.__empid = empid
        Employee.all_employees.append(self)
    def getEmpid(self):
    #print(e1.__empid)
        return self.__empid


if __name__ == '__main__':
    e1 = Employee('Jack', 'simmons', 456342)
    print(e1.fname, e1.lname)
    print(e1.getEmpid())
    print(e1.__empid)

