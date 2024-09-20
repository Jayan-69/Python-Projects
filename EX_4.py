name1 = input("Please enter your name : ")
name2 = 'Lakshitha'

print(name1)
print(name2)

print(type(name1))
print(type(name2))

print(name1[4])
print(name2[3])
print(name1[-3])
print(name1[0:3])


print()
print("------------------------------------------")
print()

name1 = input("Please enter your name : ")
print(len(name1))

for x in name1:
    print(x,end=" ")

print()
for x in range(0,5,1):
    print(name1[x],end=" ")
    
print()
print("------------------------------------------")
print()

name = input("Enter your name : ")

count = 0

for x in name:
    if x=='a':
        count += 1
print("Number of a's is", count)

















