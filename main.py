from math import sin
n = int(input("n = "))
x = float(input("x = "))
i = 1
result = 0
while (i <= n):
    result += sin(x**i)
    i += 1
print ("Result = ", result)