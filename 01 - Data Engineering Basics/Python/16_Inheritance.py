#Inheritance
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

if __name__ == '__main__':
    p1 = Person('George', 'smith')
    print(p1.fname, '-', p1.lname)
    e1 = Employee('Jack', 'simmons', 456342)
    e2 = Employee('John', 'williams', 123656)
    print(e1.fname, '-', e1.empid)
    print(e2.fname, '-', e2.empid)