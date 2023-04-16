#Conditional Statements - if
name=input("Enter Name:")
if name=="Suresh" :
    print("Hello Suresh Good Morning")
print("How are you!!!")

#Conditional Statements - if else
name=input("Enter Name:")
if name=="Suresh" :
    print("Hello Suresh Good Morning")
else:
    print("Hello Guest Good Moring")
print("How are you!!!")

cricketer=input("Enter Your Favourite Cricketer:")
if cricketer=="sachin" :
    print("God of cricket")
elif cricketer=="dhoni":
    print("Best captain")
elif cricketer=="sehwag":
    print("Fearless Cricketer")
else :
    print("not sure")

#looping
# import pdb
# pdb.set_trace()
sum=0
for i in range(4):
    print('i:',i)
    print('sum:',sum)
    sum = sum +i
    print(sum)
print(sum)

sum = 0
i=0
while i < 4:
    sum = sum+i
    print('i:',i)
    print('sum:',sum)
    i = i + 1
print('final sum:',sum)

a=['banana','apple', 'microsoft']
for element in a:
    print(element)
import pdb
pdb.set_trace()
b=[1,2,3]
for element in b:
    print(element)

b=[1,2,3]
sum = 0
for element in b:
    sum = sum + element
print(sum)

total = 0
for i in range(1,5):
    total += i
print(total)

total = 0
for i in range(1,8):
     if i%2 == 0:
        total += i
print(total)


total = 0
for i in range(1,30):
     if i%3 == 0 or i%5 ==0:
        print(i)

#To display odd numbers from 0 to 20
for x in range(21) :
    if (x % 2 != 0):
        print(x)

#To display the sum of first n numbers
n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum of first",n,"numbers is :",sum)

#Sometimes we can take a loop inside another loop,which are also known as nested loops.
for i in range(4):
    for j in range(4):
        print("i=", i, " j=", j)

#break statement
for i in range(10):
    if i==7:
        print("processing is enough..plz break")
        break
print(i)


cart=[10,20,600,60,70]
for item in cart:
    if item>500:
        print("To place this order insurance must be required")
        break
    print(item)

#continue statement : To print odd numbers in the range 0 to 9
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


