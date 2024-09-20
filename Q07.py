#display heading
print("Monthly Salary")
print("====================")
print()

#create the memory variable and assigning the values
Em_No = int(input("Enter Employee Number : "))
Em_Name = (input("Enter Employee Name : "))
H_Worked = int(input("Enter Hours Worked : "))
H_Rate = int(input("Enter Hourly Rate : "))

#find grosswage
if H_Worked > 40 :
    ADH = H_Worked - 40
    Gross_wage = 40 * H_Rate + ADH * H_Rate * float(1.5)
else:
    Gross_wage = H_Worked * H_Rate

#display result
print("---------------------")
print("Employee Number :", Em_No)
print("Employee Name :", Em_Name)
print("Gross wage :", Gross_wage)
print("=====================")
