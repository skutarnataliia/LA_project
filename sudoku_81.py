import numpy as np
from sudoku_check import check
from sudoku_read import read

n = 9
sudoku = read('sudoku2.txt', n)
solution = open('solution2.txt', 'w')

b = [0] * (n * n)
a = []

for i in range(n):
    for j in range(n):
        line = sudoku[i]
        column = [sudoku[k][j] for k in range(n)]
        b[n*i + j] = sum(column) - sum(line)
        a.append([0] * (n * n))
        for k in range(n):
            if sudoku[i][k] == 0:
                a[i*n + j][i*n + k] = a[i*n + j][i*n + k] + 1
        for k in range(n):
            if sudoku[k][j] == 0:
                a[i*n + j][k*n + j] = a[i*n + j][k*n + j] - 1

a_t = [[a[j][i] for j in range(n * n)] for i in range(n * n)]
a = []
col = 0

for i in range(n*n):
    if any(a_t[i]):
        a.append(a_t[i])
        col = col + 1

a = [[a[j][i] for j in range(col)] for i in range(n * n)]

A = np.array(a)
B = np.array(b)

rank = np.linalg.matrix_rank(A)

solution.write('Rank:' + str(rank) + ', Columns:' + str(col) + '\n')

for i in range(n * n):
    solution.write(str(a[i]) + ' ' + str(b[i]) + '\n')

A_pseudoinv = np.linalg.pinv(A)

x = np.dot(A_pseudoinv, B)

print(x)