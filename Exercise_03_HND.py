y = 0
while y<5:
    x = 0
    while x<5:
        print("*",end="")
        x=x+1
    y=y+1
    print()

print()
print("---------For Loop----------")
print()


for y in range(0,5):
    for x in range(0,y+1):
        print("*",end="")
    print()

print()
print("-----------While Loop---------")
print()

y = 0
while y<5:
    x = 0
    while x<y+1:
        print("*",end="")
        x=x+1
    y=y+1
    print()

print()
print("---------For Loop----------")
print()

for x in range(0,5):
    for y in range(x+1,6):
        print("*",end="")
    print()

print()
print("-----------While Loop---------")
print()
    
y = 0
while y<5:
    x = 5
    while x<y-1:
        print("*",end="")
        x=x-1
    y=y+1
    print()
