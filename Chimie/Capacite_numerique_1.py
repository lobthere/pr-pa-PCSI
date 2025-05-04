import numpy as np
import matplotlib.pyplot as plt

pK_a1 = 1.25
Ka1 = 10**-1.25
Ka2 = 10**-4.3
T = 298

"""--- 1 ---"""
pH = []
pas = 10000
for m in range(0, pas, 1):
    pH.append(m*14/pas)
x, y, z, w = [], [], [], []

"""--- 2 ---"""

for i in range(0, len(pH)):
    to_solve = np.array([
        [1, 1, 1],
        [-1 * Ka1, 10**(-1 * pH[i]), 0],
        [0, -1 * Ka2, 10 ** (-1 * pH[i])]
    ])

    the_values = np.array([100, 0, 0])

    the_answer = np.linalg.solve(to_solve, the_values)

    x.append(the_answer[0]/(the_answer[0] + the_answer[1] + the_answer[2])*100)
    y.append(the_answer[1]/(the_answer[0] + the_answer[1] + the_answer[2])*100)
    z.append(the_answer[2]/(the_answer[0] + the_answer[1] + the_answer[2])*100)
    w.append([the_answer[0] + the_answer[1] + the_answer[2], the_answer[0], the_answer[1], the_answer[2]])

print(w)

"""--- 3 ---"""

plt.plot(pH, x)
plt.plot(pH, y)
plt.plot(pH, z)
plt.show()
