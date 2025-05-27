
#prop qui est vrai en entré de boucle et pour toute iteration
def decomp(a):
    assert a>=1
    b = a
    n = 0
    while b%3 == 0:
        q = b//3
        n+=1
        b=q
    return (n, b)

print(decomp(1))
print(decomp(3))
print(decomp(9))
print(decomp(4))
print(decomp(12))
print(decomp(36))

"""
preuve de l algorithme:

"""