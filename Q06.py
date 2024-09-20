#display heading
print("student mark details")
print("====================")
print()

#create the memory variable and assigning the values
stid = int(input("student id : "))
stname = (input("student Name : "))
M1 = int(input("Sinhala Marks : "))
M2 = int(input("Science Marks : "))
M3 = int(input("English Marks : "))

#find total, average, grade
tot = M1+M2+M3
avg = tot/3
if avg>=65 :
   gr="pass"
else:
   gr="fail"

#display result
print("---------------------")
print("Total Marks :",tot)
print("Average Marks :",avg)
print("Grade :",gr)
print("=====================")

