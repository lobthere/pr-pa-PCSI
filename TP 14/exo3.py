"""Imports"""

from collections import deque

"""___Question 2___"""

f = open("Membres.txt", "r")

M = []


for li in f:
    li = li.strip('\n')
    l = li.split(',')
    M.append(l[1])
f.close()

#print(M)

"""___Question 3___"""

n = len(M)

f = open("Amitiés.txt")

for li in f:
    li = li.strip('\n')
    #print(li)
f.close()

"""___Question 6___"""

w = [[] for i in range(n)]

f = open("Amitiés.txt")

for li in f:
    li = li.strip('\n')
    l = li.split(',')
    w[int(l[0])].append(int(l[1]))
f.close()

#print(w)

"""___Question 7___"""

def contvide(w):
    v = []
    for i in range(len(w)):
        v.append('vide')
    return v

#print(contvide(w))

"""___Question 8___"""

def BFSd(w, O):
    pr, d = contvide(w), contvide(w)
    C = deque()
    C.append(O)
    pr[O] = 'vide'
    d[O] = 0
    while C != deque():
        P = C.popleft()
        for Q in w[P]:
            if pr[Q] == 'vide':
                C.append(Q)
                pr[Q] = P
                d[Q] = d[P] + 1
    return (d, pr)

d, pr = BFSd(w,0)
#print(d, '\n \n', pr)



def chemin(O, R, pr):

    if R == O:
        return [O]

    else:
        ch=chemin(O, pr[R], pr)
        ch.append(R)
        return ch

for i in range(0, n):
    if d[i] != 'vide':
        print(i, d[i], chemin(0, i, pr))