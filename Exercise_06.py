St_No = int(input("Enter Student Number : "))
St_Name = (input("Enter Student Name : "))
m1 = int(input("Enter Biology Marks : "))
m2 = int(input("Enter Chemistry Marks : "))
m3 = int(input("Enter Physics Marks : "))
Tot = m1 + m2 + m3
Avg = Tot/3
print("Student Number :", St_No)
print("Student Name :", St_Name)
print("Total :", Tot)
print("Average :", Avg)
if Avg > 50 :
    print('Grade = Pass')
else :
    print('Grade = Fail')