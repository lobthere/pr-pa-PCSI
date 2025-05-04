import numpy as np
import matplotlib.pyplot as plt

"""___Exercice 1___"""

pK_a1 = 1.25
Ka1 = 10**-1.25
Ka2 = 10**-4.3
T = 298

"""--- 1 ---"""
pH = []
pas = 10000
for m in range(0, pas + 1, 1):
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


"""--- 3 ---"""

plt.plot(pH, x, label='H2A')
plt.plot(pH, y, label='HA-')
plt.plot(pH, z, label='A2-')
plt.xlabel('pH')
plt.ylabel('%')
plt.title("diagramme de distribution de l'acide oxalique H2A")
plt.legend()
plt.show()




"""___Exercice 2___"""

"""--- 1 ---"""

T = 298
pKe = 14
Ks = 10**(-18.5)
C = 10**(-2)
pas = 1000

pH = []
for i in range(0, pas + 1, 1):
    pH.append(i*14/pas)

Cu , Cu2 = [], []

"""--- 2 ---"""

for i in range(0, len(pH), 1):
    HO = 10 ** (pH[i] - pKe)
    if C*(HO**2) > Ks:
        Cu2_pourcent = ((Ks/(HO**2))/C)*100
        Cu2.append(Cu2_pourcent)
        Cu.append(100-Cu2_pourcent)
    else:
        Cu2.append(100)
        Cu.append(0)

"""--- 3 ---"""

plt.plot(pH, Cu2, label='Cu2+')
plt.plot(pH, Cu, label='Cu(OH)2(s)')
plt.xlabel('pH')
plt.ylabel('%')
plt.title("diagramme de distribution de Cu2+/Cu(OH)2(s)")
plt.legend()
plt.show()

