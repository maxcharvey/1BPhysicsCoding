n = float(input("Input your number: "))
power = float(input("Which root would you like to find? "))

a = 0
b = 100

while 0.5*(b-a) > 0.0001:
    p = 0.5*(a+b)
    f_a = n - a**power
    f_p = n - p**power
    if f_a * f_p < 0:
        b = p
    else:
        a = p

print(a)
