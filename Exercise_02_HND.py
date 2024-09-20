y = 0
while y < 3:
    x = 0
    while x < 5:
        print(x)
        x=x+1
    y=y+1

print()
print("-----------------------------")
print()

x = 0
while x<5:
    x=x+1
    if x==2:
        break
    print(x)
 
print()
print("-----------------------------")
print()

print("Hello","Esoft","HND","Students")
print("Hello","Esoft","HND","Students",sep='_')
print("Hello","Esoft","HND","Students",sep='*',end='=')

print()
print("-----------------------------")
print()

print("Hello",end='-')
print("Esoft")

print()
print("-----------------------------")
print()

print("Hello","Esoft","HND","Students",sep='\n')

print()
print("-----------------------------")
print()

f = open ('abc.txt','w')
print("Hello","Esoft","HND","Students",file=f,flush=True)
