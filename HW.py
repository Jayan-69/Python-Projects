#H.W. Implement the algorithm for finding students greads in python.

a = int(input("Enter Physics marks = "))
b = int(input("Enter Combined Math marks = "))
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


