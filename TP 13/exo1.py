"""---Questions 1---"""

w = {"A": ["B", "C", "D"], "B": [], "C": ["D", "F"], "D": ["A", "B", "C", "F"], "E": ["B"], "F": ["D"]}

"""--- Question 2---"""

for P in w:
    print(P, len(w[P]))

print(" ")

"""---Question 3---"""

w = {"A": ["B", "C", "D"], "B": ["A", "D", "E"], "C": ["A", "D", "F"], "D": ["A", "B", "C", "F"], "E": ["B"], "F": ["C", "D"] }

"""---Question 4---"""

for P in w:
    print(P, len(w[P]))