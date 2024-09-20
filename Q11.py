#display headding
print("Student Mark Details")
print("==================")
print()

#using for loop
for x in range(5):
    
    #create variable and assigning the values
    St_Id = int(input("Enter Student Id : "))
    St_Name = (input("Enter Student Name : "))
    M1 = int(input("Enter Maths Marks : "))
    M2 = int(input("Enter Sinhala Marks : "))
    M3 = int(input("Enter Science Marks : "))
    M4 = int(input("Enter English Marks : "))

    #find total, average, grade
    tot = M1+M2+M3+M4
    avg = tot/4
    if avg >= 80 :
        grd = 'A'
    elif avg >= 70 :
        grd = 'B'
    elif avg >= 60 :
        grd = 'C'
    elif avg >= 50 :
        grd = 'S'
    else:
        grd = 'W'
        
    print("-----------------")
    
    #Display result
    print("Total Marks :",tot)
    print("Average Marks :",avg)
    print("Grade :",grd)
    print("==================")
    print()
