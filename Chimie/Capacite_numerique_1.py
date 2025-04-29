import matplotlib
import numpy as np

pK_a1 = 1.25
pK_a2 = 4.3
T = 298

pH = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
x, y, z = [], [], []
for i in range(0, len(pH)):
    to_solve = np.array([
        [1, 1, 1],
        [-1 * pK_a1, 10**(-1 * pH[i]), 0],
        [-1 * pK_a2, 0, 10 ** (-1 * pH[i])]
    ])

    the_values = np.array([100, 0, 0])

    the_answer = np.linalg.solve(to_solve, the_values)
    x.append(the_answer[0])
    y.append(the_answer[1])
    z.append(the_answer[2])
print(x)
