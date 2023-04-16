#Polymorphism
import pdb
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Employee(Person):
    all_employees = []
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
    def getSalary(self):
        return 'You get Monthly salary.'
    def getBonus(self):
        return 'You are eligible for Bonus.'

class ContractEmployee(Employee):
    def getSalary(self):
        return 'You will not get Salary from Organization.'
    def getBonus(self):
        return 'You are not eligible for Bonus.'

if __name__ == '__main__':
    #pdb.set_trace()
    e1 = Employee('Jack', 'simmons', 456342)
    e2 = ContractEmployee('John', 'williams', 123656)
    print(e1.getBonus())
    print(e2.getBonus())