print("-----Working with list-----")
print()

mylist = [1,2,3,4,5,6,7,8,9,10]
mytuple = [1,2,3,4,5,6,7,8,9,10]

print(mylist)
print(mytuple)
print(type(mylist))
print(type(mytuple))

print()
print("------------------------------------------------------")
print()

list1 = ['Physics','Maths','Chemistry',2000,2004,10.55,True]
print(list1[0:4])
print(list1[:5])
print(len(list1))

print()
print("-----Printing list with for loop-----")
print()

for x in range(0,len(list1)):
    print(list1[x])

print()

for x in list1:
    print(x)

print()
print("-----Generating a list of numbers using range-----")
print()

generatedlist = list(range(20,45))
print(generatedlist)
print(type(generatedlist))

print()
print("-----List methods-----")
print()

mylist = [10,20,30,40,50]
print(mylist)

mylist.append(55)
print(mylist)

poppeditem = mylist.pop()
print(mylist)
print(poppeditem)

mylist.insert(2,77)
print(mylist)

mylist.insert(0,90)
print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

print(mylist.count(10))

mylist2 = [100,2300,300]
mylist.extend(mylist2)
print(mylist)

mylist.clear()
print(mylist)





