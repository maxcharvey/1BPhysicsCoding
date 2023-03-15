# This piece of code is a risk roller for the game 'risk'.
# It can be used to automate the outcomes of large scale attacks to speed up the game

import random

A = int(input("Number of attacking troops "))
D = int(input("Number of defending troops "))

while A and D > 0:
    if A == 2:
        A_num = [random.randint(1, 6) for i in range(2)]
    elif A == 1:
        A_num = [random.randint(1, 6) for i in range(1)]
    else:
        A_num = [random.randint(1, 6) for i in range(3)]

    if D == 1:
        D_num = [random.randint(1, 6) for i in range(1)]
    else:
        D_num = [random.randint(1, 6) for i in range(2)]

    A_num.sort(reverse=True)
    D_num.sort(reverse=True)

    for i in range(min(len(A_num), len(D_num))):
        if D_num[i] >= A_num[i]:
            A = A-1
        elif D_num[i] < A_num[i]:
            D = D-1

print(f'Number of attacking troops remaining = {A}')
print(f"Number of defending troops remaining = {D}")
