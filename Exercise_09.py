Em_No = int(input("Enter Employee Number : "))
Em_Name = (input("Enter Employee Name : "))
So_Q = int(input("Enter Sold Quantity : "))
U_Pr = int(input("Enter Unit Price : "))
TSV = So_Q * U_Pr
if TSV > 100000:
    Commission = TSV * 20 / 100
elif TSV > 75000 :
    Commission = TSV * 15 / 100
elif TSV > 50000 :
    Commission = TSV * 10 / 100
else :
    Commission = TSV * 5 / 100
print("Employee Number :", Em_No)
print("Employee Name :", Em_Name)
print("commission :", Commission)
