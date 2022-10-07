word_1 = "paraparaparadise"

word_2 = "paragraph"

X = set([word_1[i] + word_1[i + 1] for i in range(len(word_1) - 1)])
Y = set([word_2[i] + word_2[i + 1] for i in range(len(word_2) - 1)])

print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))
print(Y.difference(X))
print("se" in X.intersection(Y))