x = int (input("Enter the value = "))
if x % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print()
print("=====================================")
print()

a = int(input("Input A = "))
b = int(input("Input B = "))

if a > b:
    print("A is greater than B")

elif a < b:
    print("A is less than B")
else:
    print("A is equal to B")

print()
print("=====================================")
print()

#H.W. Implement the algorithm for finding students greads in python.

a = int(input("Enter Physics marks = "))
b = int(input("Enter Combined math marks = "))
c = int(input("Enter Chemistry marks = "))

avg = (a + b + c) / 3
print(avg)

if avg > 75:
    print("A")
elif avg > 65:
    print("B")
elif avg > 55:
    print("C")
elif avg > 35:
    print("S")
else:
    print("F")

print()
print("=====================================")
print()

x = 0
while x < 5:
    print(x)
    x = x + 1

print()
print("=====================================")
print()

for x in range(0,5,1):
    print(x)

print()
print("=====================================")
print()

#print numbers from 0 to 10 using while loop

x = 0
while x <= 10:
    print(x)
    x = x + 1

print()
print("=====================================")
print()

#print numbers from 50 to 40 using while loop

#x = 50
# print(x)
 #   x = x + 1








