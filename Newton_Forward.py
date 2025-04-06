#Newton Forward

def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp

def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def main():
    n = 4
    x = [1, 1.5, 2, 2.5]
   
    y = [[0] * n for _ in range(n)]
    y[0][0] = 2.71823
    y[1][0] = 4.4817
    y[2][0] = 7.3891
    y[3][0] = 12.1825

    for i in range(1, n):
        for j in range(0, n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    for i in range(n):
        print("{:4}".format(x[i]), end="\t")
        for j in range(n - i):
            print("{:4}".format(y[i][j]), end="\t")
        print()

    coefficients = [y[0][0]]
    for i in range(1, n):
        coefficients.append(y[0][i] / fact(i))

    print("\nPolynomial:")
    print("f(x) =", coefficients[0], end=" ")
    for i in range(1, n):
        print("+", coefficients[i], end="")
        for j in range(i):
            print("(x - {:f})".format(x[j]), end="")
    print()

    value = 2.25
    sum_ = y[0][0]
    u = (value - x[0]) / (x[1] - x[0])
    for i in range(1, n):
        sum_ = sum_ + (u_cal(u, i) * y[0][i]) / fact(i)

    print("\nValue at", value, "is", sum_)

if __name__ == "__main__":
    main()