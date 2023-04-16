#basic datatypes
import pdb

print('Type of 4 is                         :',type(4))
print('Type of 4.0 is                       :',type(4.0))
print('Type of -4 is                        :',type(-4))
print('Type of 1j is                        :',type(1j))
print('Value of int 5 converted to float    :',float(5))
print('Value of decimal 44 with precision   :',float(44.555555555))
print(7.6+8.7)
print(round(7.6+8.7))
print(round(7.6+8.7,1))
print(round(1.1+1.1+1.1,1) == 3.3)
#--------------------------------Basic Arithmetic Operators
a=7.0
b=11.0
c=7
d=11

print(a + b)
print(a-b)
print(a*b)
print(a/b)
print(c/d)
# power
print(c**2)
#reminder
print(d%c)
#-------------------------------------Basic Conditional Operators(Relational and Equality Operators)
a=3
b=5
pdb.set_trace()
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(type(True))
print(bool(28))
print(bool(-2.7))
print(bool(0))
print(bool('Jagadeesh'))
print(bool(" "))
print(bool("."))
print(bool(""))
print(str(False))
print(int(True))
print(5 + True)
print(5 * True)
print(5 * False)



