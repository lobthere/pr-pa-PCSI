def triselectionechange(t):
    n=len(t)
    for i in range(n-1):
        m=t[i]
        k = i
        for j in range(i+1, n):
            if t[j] < m:
                m = t[j]
                k = j
        t[i], t[k] = t[k], t[i]