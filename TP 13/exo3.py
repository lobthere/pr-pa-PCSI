"""---Question 1---"""

w = {"A": {"B": 3, "C": 2, "D": 4},
     "B": {},
     "C": {"D": 1, "F": 3},
     "D": {"A": 3, "B": 2, "C": 2, "F": 1},
     "E": {"B": 1},
     "F": {"D": 2} }

print(w)

"""---Question 2---

[A,C,F] = 5
[A,D,F] = 5
[A,C,D,F] = 4
[A,D,C,F] = 9
plus court chemin : [A,C,D,F] = 4, d(A,F) = 4

"""

"""---Question 3---"""

w = [{1: 3, 2: 2, 3: 4},
     {},
     {3: 1, 5: 3},
     {0: 3, 1: 2, 2: 2},
     {1: 1},
     {3: 2}
     ]

print(w)

"""---Question 4---"""

M = [[v, 3, 2, 4, v, v],
     [v, v, v, v, v, v],
     [v, v, v, 1, v, 3],
     [3, 2, 2, v, v, 1],
     [v, 1, v, v, v, v],
     [v, v, v, 2, v, v]]
M = np.array(M)
print(M)