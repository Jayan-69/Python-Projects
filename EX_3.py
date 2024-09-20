a = 10
while a <= 15:
    a += 1
    if a == 12:
        continue
    print(a)

print()
print("----------------------------")
print()

a = 10
while a <= 15:
    a += 1
    if a == 12:
        break
    print(a)

print()
print("----------------------------")
print()

for c in "Jayan":
    if c == "a":
        print("a")
    else:
        print(c)

print()
print("----------------------------")
print()

name = input("Please enter your name : ")
for c in name:
    print(c)
else:
    print("The name is printed")

print()
print("----------------------------")
print()

x = 10
y = 20
z = 30
print(x,y,z,sep="-")

print()
print("----------------------------")
print()

print(x, end="\n")
print(y, end="\n")
print(z, end="\n")

print()
print("----------------------------")
print()

f = open("D:/test.txt",'w')
print("Hello",file=f,flush=True)







