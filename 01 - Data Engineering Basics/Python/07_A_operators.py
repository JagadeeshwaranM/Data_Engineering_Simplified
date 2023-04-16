import pdb

#----------------Logical Operator example 1
a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

#---------Assignment Operators
pdb.set_trace()
x=10
x+=20
print(x)

#---------------Ternary Operators

a=10
b=20
x=30 if a<b else 40
print(x)

#-------Special Operators Identity Operator

a=10
b=10
print(a is b)

x=True
y=True
print( x is y)

a="suresh"
b="suresh"
print(id(a))
print(id(b))
print(a is b)

list1=["one","two","three"]
list2=["one","two","three"]
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)

#----Special Operator Membership Operator


x="hello learning Python is very easy!!!"
print('h' in x)
print('d' in x)
print('d' not in x)
print('Python' in x)


#Operator Precedence
print(3+10*2)
print((3+10)*2)
a=30
b=20
c=10
d=5
print((a+b)*c/d)
print(a+(b*c)/d)
