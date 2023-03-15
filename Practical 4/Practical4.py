# Newton-Raphson method of root finding for 2nd and 3rd order polynomials:

order = int(input("What is the order of your polynomial (max order 3): "))
p = float(input("Enter your initial guess for the root: "))
coeff = []
q = int(input("How many iterations would you like to complete? "))

for i in range(0, order + 1):
    a = int(input(f"What is the coefficient of the order {i} term "))
    coeff.append(a)


def polynomial(x):
    c = 0
    for m in range(len(coeff)):
        c += coeff[m] * x**m
    return c


def derivative(xx):
    d = 0
    for n in range(len(coeff)):
        d += n*coeff[n]*xx**(n-1)
    return d


if order == 2 and coeff[1]**2 - 4*coeff[0]*coeff[2] < 0:
    print("Your quadratic has purely imaginary roots and this program will not work!!!")
else:
    for trial in range(q):
        p = p - polynomial(p)/derivative(p)

print(f"The root after {q} iterations was found to be {p}")
