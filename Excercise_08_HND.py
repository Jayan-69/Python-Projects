print("-----Functions in python(Without return statement)-----")
print()

def add(n1,n2):
    print(n1+n2)
add(10,20)

print()
print("-----Functions in python(With return statement)-----")
print()

def addnumbers(n1,n2):
    return n1+n2

print(addnumbers(10,20))

print()
print("-----------------------------------------------------")
print()

def printnumbers(n1,n2):
    for x in range(n1,n2):
        print(x)

printnumbers(50,60)
print()
printnumbers(10,40)
print()
printnumbers(69,225)

print()
print("-----------------------------------------------------")
print()

def printsuminrange(start,end):
    sum=0
    for count in range(start,end):
        sum=sum+count
    print(sum)

printsuminrange(11,15)

print()
print("-----------------------------------------------------")
print()

def area(pi,radius):
    a = pi*radius*radius
    return a

piconstant = 3.1415
radiusofcircle = 7

areaofthecircle = area(piconstant,radiusofcircle)

print(areaofthecircle)
    
print()
print("-----Call by value function-----")
print()

def changenumber(num):
    num=num+10

n = 100
print("Number before function call",n)
changenumber(n)
print("Number after function call",n)

print()
print("-----Pass by value function-----")
print()

def changelist(mylist):
    mylist.append(10)

numbers = [10,20,30,40,50]
print("Numbers list before function call",numbers)
changelist(numbers)
print("Numbers list after function call",numbers)
