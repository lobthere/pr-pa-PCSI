def evahor(l: list,x: int):
    n=len(l)
    y = l[n-1]
    for k in range(n-2, -1, -1):
        y = l[k]+x*y
    return y

print(evahor([2, 5, 1],3))