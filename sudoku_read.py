def read(filepath):

    file = open(filepath, 'r')

    sudoku = []
    for i in range(9):
        line = file.readline()
        sudoku.append(list(map(int, line.split())))
    
    file.close()

    return sudoku