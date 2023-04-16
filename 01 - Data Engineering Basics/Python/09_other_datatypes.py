#other datatypes
#--------------------------------Collection and Mappings types in Python
#Range Type and function, set type and dictionary
import pdb
a=list(range(6))
print(a)
b=list(range(2,6))
print(b)
c=tuple(range(6))
print(c)
d=tuple(range(2,6))
print(d)
e=list(range(0,11,2))
print(e)
############ give empty list
e=list(range(11,2))
print(e)
e=list(range(-2,-11,2))
print(e)
###########corrected
e=list(range(11,20))
print(e)
e=list(range(-2,-11,-2))
print(e)

##################set elements  Order does not matter and data needs to be unique

a={1,'s',7.8}
print(a)
b=set([1,'B',6.9,1])
print(b)
b.add(5)
print(b)
c=set()
print(c)
print(dir(c))
My_set = {1,'s',7.8}
print(len(My_set))
for a in My_set:
     print(a)
c={1,2,3,4}
print(c)
d=set([1,2,3,4])
print(d)
e=set()
e.add(5)
for a in e:
     print(a)
e.update([6,3])
print(e)
e.remove(5)
print(e)
for a in e:
     print(a)
e.discard(6)
print(e)
e.discard(10)
print(e)
e.pop()
print(e)

a={1,2,3,4}
b={1,5,4,6}
c={9,10}
print(a|b)
print(a.union(b,c))
a={1,2,3,4}
b={1,5,4,6}
print(a&b)
print(a.intersection(b))
a={1,2,3,4}
b={1,2,7,8}
print(a-b)
print(a.difference(b))

#############-------------------- Frozen set A frozen set is a set whose values cannot be modified
a={1,2,3}
print(type(a))
b=frozenset(a)
print(type(b))
print(b)
#############-------------------- Dictionary Type
a={'john':150,'mac':200}
print(a['john'])
a['john']=900
print(a)
del a['mac']
print(a)
print(a.keys())
#####################
a=[]
print(type(a))
print(a)
b=set()
print(type(b))
print(b)
c=set([])
print(type(c))
print(c)
d=tuple()
print(type(d))
print(d)
e={}
print(type(e))
print(e)
f=()
print(type(f))
print(f)
a=[]
b={}
c=()
d=set()
print(type(a))
print(type(b))
print(type(c))
print(type(d))
a.append([3,6,7,8])
print(a)

b={'key1':'geeks', 'key2':'for'}
b.update({'key3':'geeks'})
print(b)
b['key3']='jack'
print(b)


d.add('a')
print(d)
d.update(('b','c','d'))
print(d)
d.add('a')
print(d)
d.add('b')
print(d)
d.update('c')
print(d)
d.add('d')
print(d)
