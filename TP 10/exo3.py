def partition(t):
    n = len(t)
    i = 0
    j = n-1
    while i <= j:
        if t[i] < 0:
            i+=1
        else:
            t[i],t[j] = t[j], t[i]
            j=j-1
    return i

t = [-1, -3, 4, 1, 0, 2, -4, 1]
print(t)
print(partition(t))
print(t)