#sequence datatypes
#mutable - List, Set, Dictionary
#Immutable - String, Tuple
import pdb

#-------------------------------------------- String
welcome = "Hello World"
print(welcome)
print(welcome[0])
print(welcome[-11])
print(welcome[-1])
s='abcd'
print(s[0])
# s[0]='1'
# Gives error as we can't change s[0] as it is immutable type
#------------------------------------------- String

s='abcd'
s += 'efgh'
print(s)
print(s)
#
s='abcd'
s='efgh'
print(s)
a='123'
print(a[0])
print(a)
a='453'
print(a[0])
print(a)
########--------------------------LIST Datatype MUTABLE
a=[12,'demo',12.2]
print(a)
print(a[0])
a[0]=24
print(a)
a.append('jagadeesh')
print(a)
a.extend(['satheesh','suresh'])
a[0]='twelve'
print(a)
del a[0]
print(a)
print(a[0:2])
print(a[0:])
a=[]
a.append(12)
print(a)

###############--------------------------TUPLE Datatype IMMUTABLE
a=(12,23)
print(a)
b=(12,23,'Jaga')
print(b)
print(b[0])
#b[0]=11
print(b)
len(b)
print(b[0:2])

#---------------------------- Slicing in List and String

my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[0])
print(my_list[5])
print(my_list[-1])
print(my_list[-10])
print(my_list[0:6])
print(my_list[3:8])
print(my_list[-7:-2])
print(my_list[1:9])
print(my_list[1:])
print(my_list[:-1])
print(my_list[:])
#-------------------- using step func

print((my_list[2:-1:2]))
print(my_list[-1:2:-1])
print(my_list[-2:1:-2])
print(my_list[::-2])
pdb.set_trace()
print(my_list[::-1])
print(my_list[::1])