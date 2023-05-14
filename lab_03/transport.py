a = [40, 30, 20]
b = [30, 25, 18, 20]

D = [[1, 2, 6, 4], [3, 1, 3, 2], [5, 7, 5, 1]]
# print(linprog(a,b,D))
if sum(a) != sum(b):
    a.append(sum(b)-sum(a))
    D.append([0, 0, 0, 0])
    # print(D)


temp = []
for i in range(4):
    new_matrix = []
    for j in range(4):
        if a[j] > b[j]:
            new_matrix += [b[j], a[j]-b[j]]
            # print(new_matrix)

        # func = D[i][j] * matr[i][j]
temp += new_matrix
print(temp)
# print(new_matrix)