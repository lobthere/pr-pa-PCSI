"""___exo 1___"""
#1
def evalpol3(l: list, x: int):
    n = len(l)
    s=l[0]
    for k in range(1, n):
        s = s+l[k]*(x**k)
    return s
#2
print(evalpol3([2, 5, 1],3))

