Em_No = int(input("Enter Employee Number : "))
Em_Name = (input("Enter Employee Name : "))
Gen = (input("Enter Your Gender : "))
B_Sal = int(input("Enter Basic Salary : "))
if Gen == 'Female':
    Tax = B_Sal * 10/100
else:
    Tax = B_Sal * 15/100
print("Employee Number :", Em_No)
print("Employee Name :", Em_Name)
print("Basic Salary :", B_Sal)
print("Tax :", Tax)
