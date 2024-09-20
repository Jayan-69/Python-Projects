St_No = int(input("Enter Student Number : "))
St_Name = (input("Enter Student Name : "))
m1 = int(input("Enter Biology Marks : "))
m2 = int(input("Enter Chemistry Marks : "))
m3 = int(input("Enter Physics Marks : "))
m4 = int(input("Enter English Marks : "))
Tot = m1 + m2 + m3 + m4
Avg = Tot/4
print("Student Number :", St_No)
print("Student Name :", St_Name)
print("Total :", Tot)
print("Average :", Avg)
if Avg > 80 :
    print('Grade = A')
elif Avg > 70 :
    print('Grade = B')
elif Avg > 60 :
    print('Grade = C')
elif Avg > 50 :
    print('Grade = S')
else :
    print('Grade = Fail')

