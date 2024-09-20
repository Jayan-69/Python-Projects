def changelist (mylist):
    mylist.append(10)

def add(n1):
    print(n1)
    n1 = n1 + 10
    print(n1)

x = 10
print("Value of X befor function call", x)
add(x)
print("Value of X after function call", x)

def changelist (mylist):
    print(mylist)
    mylist.append(10)
    print(mylist)

y = [10,20,30,40,50]
print("Value of y befor function call", y)
changelist(y)
print("Value of y after function call", y)
