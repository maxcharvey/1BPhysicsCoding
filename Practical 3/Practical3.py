import math
import random
import matplotlib.pyplot as plt


def approximator(n):
    count = 0
    iterations = []
    values = []
    for i in range(n):
        x = random.uniform(1, 2)
        y = random.uniform(0, 1)
        test = x * y
        if test <= 1:
            count += 1
        else:
            count = count

        fraction = count / (i + 1)

        values.append(fraction)
        iterations.append(i + 1)
    return values, iterations


fig, ax1 = plt.subplots(figsize=(12, 8), nrows=2, ncols=2)
ax1 = ax1.flatten()
N = [10, 100, 10000, 10000000]

for j in range(4):
    a, b = approximator(N[j])
    ax1[j].plot(b, a, "k-", label="Numerical ln(2) ")
    ax1[j].plot([0, b[-1]], [math.log(2), math.log(2)], "r-", label="Actual ln(2) ")
    ax1[j].set_xlabel('Iteration number')
    ax1[j].set_ylabel('Approximate value of ln(2)')
    ax1[j].set_title(f'Approximating ln(2) using {N[j]} iterations', fontsize=9)
    ax1[j].text(0.95, 0.1, f'Value after {N[j]} iterations = {a[-1]}', transform=ax1[j].transAxes, ha='right')
    ax1[j].legend(loc="upper right")

plt.tight_layout()
fig.suptitle('Approximation of ln(2) using the Monte Carlo method', y=1.05, fontsize=16)
plt.show()
