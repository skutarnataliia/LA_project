def check(sudoku):

    for i in range(9):
        if sum(sudoku[i]) != 45:
            return 'Line ' + str(i)

    for i in range(9):
        summ = 0
        for j in range(9):
            summ = summ + sudoku[j][i]
        if summ != 45:
            return 'Column ' + str(i)
    
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            if sudoku[i][j] + sudoku[i+1][j] + sudoku[i+2][j] + sudoku[i][j+1] + sudoku[i+1][j+1] + sudoku[i+2][j+1] + sudoku[i][j+2] + sudoku[i+1][j+2] + sudoku[i+2][j+2] != 45:
                return 'Square ' + str(i/3 + 1 + j/3)
    
    return 'Good!'