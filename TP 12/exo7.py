"""___Exercice 7___"""

def nbracines(a: float, b: float, c: float):
    delta = b**2 - 4*a*c
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else :
        return 2

print(nbracines(1.0, 6.0, 9.0))
print(nbracines(0.1, 0.6, 0.9))
print(nbracines(.000001, .000006, .000009))