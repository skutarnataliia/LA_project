from sympy import groebner, symbols
x = [symbols('x%d' % i) for i in range(81)]

sudoku = [0,3,0,0,0,0,0,0,0,
          0,0,0,1,9,5,0,0,0,
          0,0,8,0,0,0,5,6,7,
          8,0,0,0,6,0,0,0,0,
          4,0,0,8,0,0,0,0,1,
          0,0,0,0,2,0,0,0,0,
          0,6,0,0,0,0,2,8,0,
          0,0,0,4,1,9,0,0,5,
          0,0,0,0,0,0,0,7,0]
# sudoku = [
#     0, 2, 5, 3, 4, 7, 9, 8, 6,
#     3, 4, 0, 9, 6, 8, 5, 2, 1,
#     6, 0, 9, 7, 2, 1, 4, 5, 3,
#     2, 1, 6, 5, 3, 0, 7, 9, 8,
#     5, 7, 4, 0, 9, 3, 1, 6, 0,
#     8, 9, 3, 6, 1, 5, 2, 7, 4,
#     4, 0, 1, 2, 8, 9, 3, 1, 5,
#     7, 6, 8, 0, 0, 2, 6, 3, 9,
#     9, 5, 2, 4, 7, 6, 8, 4, 7
# ]




# % solution = [5,3,4,6,7,8,9,1,2,
# %             6,7,2,1,9,5,3,4,8,
# %             1,9,8,3,4,2,5,6,7,
# %             8,5,9,7,6,1,4,2,3,
# %             4,2,6,8,5,3,7,9,1,
# %             7,1,3,9,2,4,8,5,6,
# %             9,6,1,5,3,7,2,8,4,
# %             2,8,7,4,1,9,6,3,5,
# %             3,4,5,2,8,6,1,7,9]

F=[]

# Restrict values to 1-9
print('1')
for xi in x:
  F.append((xi-1)*(xi-2)*(xi-3)*(xi-4)*(xi-5)*(xi-6)*(xi-7)*(xi-8)*(xi-9))

# Sum of lines = 45
print('2')
for i in range(0,80,9):
  F.append(x[i]+x[i+1]+x[i+2]+x[i+3]+x[i+4]+x[i+5]+x[i+6]+x[i+7]+x[i+8]-45)
print('3')
for i in range(9):
  F.append(x[i]+x[i+9]+x[i+18]+x[i+27]+x[i+36]+x[i+45]+x[i+54]+x[i+63]+x[i+72]-45)
# Product of lines = 362880
print('4')
for i in range(0,80,9):
  F.append(x[i]*x[i+1]*x[i+2]*x[i+3]*x[i+4]*x[i+5]*x[i+6]*x[i+7]*x[i+8]-362880)
print('5')
for i in range(9):
  F.append(x[i]*x[i+9]*x[i+18]*x[i+27]*x[i+36]*x[i+45]*x[i+54]*x[i+63]*x[i+72]-362880)

# Blocks sum to 45
print('6')
for i in [0,3,6,27,30,33,54,57,60]:
  F.append(x[i]+x[i+1]+x[i+2]+x[i+9]+x[i+10]+x[i+11]+x[i+18]+x[i+19]+x[i+20]-45)
# Product of numbers in blocks = 362880
print('7')
for i in [0,3,6,27,30,33,54,57,60]:
  F.append(x[i]*x[i+1]*x[i+2]*x[i+9]*x[i+10]*x[i+11]*x[i+18]*x[i+19]*x[i+20]-362880)
print('8')
for count, val in enumerate(sudoku):
  if val != 0:
    F.insert(0,x[count]-val)
print('9')
G = groebner(F)
print('10')

solution = [G.reduce(p)[1] for p in x]

# Reshape solution into a Sudoku grid
solution_grid = []
for i in range(0, 81, 9):
    solution_grid.append(solution[i:i+9])

# Print solution
for row in solution_grid:
    print(row)
    