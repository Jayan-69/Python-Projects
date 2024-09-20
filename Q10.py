#display heading
print("Salary and Tax")
print("====================")
print()

#create the memory variable and assigning the values
Em_No = int(input("Enter Employee Number : "))
Em_Name = (input("Enter Employee Name : "))
Gen = (input("Enter Your Gender : "))
B_Sal = int(input("Enter Basic Salary : "))

#find tax 
if Gen == 'Female':
    Tax = B_Sal * 10/100
else:
    Tax = B_Sal * 15/100

#display result
print("Employee Number :", Em_No)
print("Employee Name :", Em_Name)
print("Basic Salary :", B_Sal)
print("Tax :", Tax)
