
"""___Question 1___"""

pr = {"B": "A", "C": "A", "D": "B", "E": "B", "F": "C", "G": "D"}
print(pr)

"""___Question 2___"""

def chemin(O, R, pr):

    if R == O:
        return [O]

    else:
        ch=chemin(O, pr[R], pr)
        ch.append(R)
        return ch

for R in pr.keys():
    print(chemin('A', R, pr))