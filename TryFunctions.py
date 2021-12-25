import math

x = 0
z = 0
for i in range(2,9):
    if i % 2 == 0:
        a = 1 / i * -1
        x = x + a
        #print(a)
    else:
        b = 1 / i
        z = z + b
        #print(b)
#print(x,z)
y = 1 + x + z
print(y)


y_2 = 1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 + 1/7 - 1/8

print(y_2)