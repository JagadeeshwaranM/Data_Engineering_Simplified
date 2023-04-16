#Iterator
import pdb
pdb.set_trace()
#--------------------Iterator
x=[1,2,3]
for i in x:
    print(i)

x=[1,2,3]
iter1=iter(x)
print(next(iter1))
print(next(iter1))

x=[1,2,3]
iter1=iter(x)
while True:
    try:
        print(next(iter1))
    except StopIteration:
        break






