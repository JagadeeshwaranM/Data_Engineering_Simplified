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
   

# ----------------------------------------------------------------

# there are four types of inheritance in Oops concept. Let's go through all of them.

# Let's first understand simple inheritance
class All_calculation:  # it's called parent class
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(f'addition of two given number is {self.a + self.b}')

    def substraction(self):
        return f'substraction of two given number is {self.a - self.b}'


class Number(All_calculation):  # it's called subclass or drived class or child class

    def multi(self):
        return f'multification of two given number is {self.a * self.b}'


obj = Number(3, 2)
obj.add()
obj = All_calculation(1, 2)
obj.substraction()


# -----------------------------------------------------------------------------------------------------------------

# Now, let's understand Multi-level Inheritance

class car:  # Grand class
    def __init__(self, name, com):
        self.name = name
        self.com = com

    def color(self):
        print('This is black car')


class speed(car):  # Parent class
    def speed(self):
        print(f'if car name is {self.name} and company is {self.com}, speed is 100 km/h')

    def doors(self):
        print('this is two seaters car, So it may have two doors.')


class shape(speed):  # child class
    def shape(self):
        print(f'if speed is 100km/hour, car shape might be sedan')

    def Buyer(self):
        print(f'buyer must have down payment near 10 lacs.')


obj = shape('Sedan', 'Mercedese')
obj.Buyer()
obj.speed()
obj.color()


# --------------------------------------------------------------------------------------------------------------------------


# Now, let's understand Multiple Inheritance

class standard:  # Parent class
    def __init__(self, name, std):
        self.name = name
        self.std = std

    def fees(self):
        print(f'standard of {self.std} is $7000')


class Subject:  # Parent class
    def sub(self):
        print('student has to learn total main three subjects')

    def sub_name(self):
        print('"Math", "Science", "English", "Sanskrit"')


class Student(standard, Subject):  # Child class, inherited from multiple class
    def Uniform(self):
        print(f'students have to wear white shirt and blue trouser')

    def Leave(self):
        print(f'Student can take leave three days off for sick')


obj = Student('Bhavik', 7)
print(obj.std)
obj.fees()
obj.sub_name()
obj.Leave()

# -------------------------------------------------------------------------------------------------------------------------


# Now let's understand the hierarchical inheritance

class provide_email:  # parent class
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.name = 'bhavik'

class login(provide_email):  # child class
    def login_detail(self):
        if self.email == 'gajerabhavik915':
            print('you are successfully logged in')
        else:
            print('please provide correct email')

    def check_balance(self):
        self.login_detail()
        if self.email == 'gajerabhavik915':
            print('your available balance is $200000')
        else:
            print('first log in, check your balance')


class create_account(provide_email):  # child class
    def create_acc(self):
        if self.email == 'gajerabhavik915':
            print('your account is successfully created')
        else:
            print('please provide bhavik\'s email')

    def check_balance(self):
        self.create_acc()
        if self.email == 'gajerabhavik915':
            print('your available balance is $200000')
        else:
            print('first log in, check your balance')


# obj = create_account('gajerabhavik915', 7573073)
# # obj.create_acc()
# obj.check_balance()

obj1 = login('gajerabhavik915', 7573073)
obj1.login_detail()
   
