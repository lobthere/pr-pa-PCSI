"""imports"""

import numpy as np


"""---Questions 1---"""

w = [[1, 2, 3],
     [0, 3, 4],
     [0, 3, 5],
     [0, 1, 2, 5],
     [1],
     [2, 3]]

"""---Questions 2---"""

for i in range(len(w)):
    print(i, w[i])

"""---Questions 3---"""

def litomat(w):
    n = len(w)
    M = np.array([[0 for j in range(n)] for i in range(n)])
    for i in range(n):
        for j in w[i]:
            M[i, j] = 1
    return M

print(litomat(w))

"""---Question 4---"""

M = np.array([[0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 1],
 [1, 1, 1, 0, 0, 1],
 [0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0]])

print(M)

"""---Question 5---"""

def degs(M, i):
    sum = 0
    for j in range(len(M)):
        sum += M[i][j]
    return sum

for i in range(len(M)):
    print(i, degs(M, i))

"""---Question 6---"""
"""
def mattoli(M):
    w = []
    for i in range(len(M)):
        for j in range(len(M[i])-1):
            if M[i][j] == 1:
                try :
                    w[i].append(j)
                except IndexError:
                    w.append([])
                    w[i].append(j)
            elif degs(M, i) == 0:
                w.append([])
    return w
"""
def mattoli(M):
    w = []
    for i in range(len(M)):
        wi = []
        for j in range(len(M)):
            if M[i][j] == 1:
                wi.append(j)
        w.append(wi)
    return w

print(mattoli(M))


