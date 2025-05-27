"""imports"""

from collections import deque


"""___Question 1___"""

w = {"A": ['B', 'C'],
    "B": ['C', 'D', 'E'],
    "C": ['B', 'D', 'F'],
    'D': ['E', 'F', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['D'],
    'H': ['G'],
    'I': ['G'] }

for P in w.keys():
    print(P, w[P])

print('\n')

for P in w.keys():
    for Q in w[P]:
        print(P, Q)


"""___Question 2___"""

def contvide(w):
    v = {}
    for i in w:
        v[i] = 'vide'
    return v

print(contvide(w))

"""___Question 3___"""

def BFSd(w, O):
    pr, d = contvide(w), contvide(w)
    C = deque()
    C.append(O)
    pr[O] = '-'
    d[O] = 0
    while C != deque():
        P = C.popleft()
        for Q in w[P]:
            if pr[Q] == 'vide':
                C.append(Q)
                pr[Q] = P
                d[Q] = d[P] + 1
    return (d, pr)

d, pr = BFSd(w, 'A')

print(d)
print(pr)


"""___Question 4___"""


def chemin(O, R, pr):

    if R == O:
        return [O]

    else:
        ch=chemin(O, pr[R], pr)
        ch.append(R)
        return ch

for R in pr.keys():
    if pr[R] != 'vide':
        print(R, d[R], chemin('A', R, pr))