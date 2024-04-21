def read(filepath, n):

    file = open(filepath, 'r')

    sudoku = []
    for i in range(n):
        line = file.readline()
        sudoku.append(list(map(int, line.split())))
    
    file.close()

    return sudoku