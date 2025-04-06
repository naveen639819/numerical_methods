#Gauss Forward

import numpy as np

def p_cal(p, n):

    for i in range(1, n):
         if(i%2==1):
             p * (p - i)
         else:
             p * (p + i)
    return p;
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

n = 7;
x = [ 1, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30 ];

y = [[0 for i in range(n)]
        for j in range(n)];
y[0][0] = 2.7183;
y[1][0] = 2.8577;
y[2][0] = 3.0042;
y[3][0] = 3.1582;
y[4][0] = 3.3201;
y[5][0] = 3.4903;
y[6][0] = 3.6693;

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

value = 1.17;

sum = y[int(n/2)][0];
p = (value - x[int(n/2)]) / (x[1] - x[0])

for i in range(1,n):
    sum = sum + (p_cal(p, i) * y[int((n-i)/2)][i]) / fact(i)

print("\nInterpolated value, using Gauss forward interpolation, at", value, "is", sum )