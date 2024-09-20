n = input("Input : ")
n = [int(i) for i in n.split("")]
y, m, d = n[0], n[1], n[2]

if m<3:
    m = m + 12
    y = Y - 1

a = 2 * m + 6 * (m + 1) // 10
b = y + y // 4 - y // 100 + y // 400
f_1 = d + a + b + 1
f = f_1 % 7

print (a)

