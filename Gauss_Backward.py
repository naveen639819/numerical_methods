#Gauss Backward

import numpy as np

def p_cal(p, n):

    for i in range(1, n):
         if(i%2==1):
             p * (p + i)
         else:
             p * (p - i)
    return p;

def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

n = 4;
x = [12500, 12510, 12520, 12530];

y = [[0 for i in range(n)] for j in range(n)];
y[0][0] = 111.803399;
y[1][0] = 111.848111;
y[2][0] = 111.892806;
y[3][0] = 111.937483;

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = (y[j + 1][i - 1] - y[j][i - 1])

value = 12516;

sum = y[int(n/2)][0];
p = (value - x[int(n/2)]) / (x[1] - x[0])

for i in range(1,n):
    sum = sum + (p_cal(p, i) * y[int((n-i)/2)][i]) / fact(i)

print("\nInterpolated value, using Gauss backward interpolation, at", value, "is", sum )