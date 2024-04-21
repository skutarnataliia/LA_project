import numpy as np

def get_a_cell(N):
    cells = np.zeros((N**2, N**3))
    for i in range(N**2):
        startpos = i * N
        cells[i, startpos:startpos + N] = 1
    return cells

def get_a_box(N):
    Inxn = np.eye(N)
    Jn = np.tile(Inxn, (1, int(np.sqrt(N))))
    box1 = np.tile(Jn, (int(np.sqrt(N)), 1))
    rest = box1.shape[1]
    box1 = np.hstack((box1, np.zeros((N, N**3 - rest))))

    box_rest = []
    base = Jn.shape[1]
    for row in range(1, N):
        box_temp = np.hstack((np.zeros((N, row * base)), np.tile(Jn, (int(np.sqrt(N)), 1))))
        rest = box_temp.shape[1]
        box_temp = np.hstack((box_temp, np.zeros((N, N**3 - rest))))
        box_rest.append(box_temp)
    box_rest = np.vstack(box_rest)
    res = np.vstack((box1, box_rest))
    return res

def get_a_col(N):
    Inxn = np.eye(N)
    Ocoln = np.zeros((N, N**2 - N))
    col1 = np.tile(np.hstack((Inxn, Ocoln)), (1, N))
    cols_mid = []
    for row in range(1, N-1):
        col_temp = np.hstack((np.zeros((N, N*row)), np.tile(np.hstack((Inxn, Ocoln)), (1, N-1)), Inxn))
        col_temp = np.hstack((col_temp, np.zeros((N, (N**2 - N) - N*row))))
        cols_mid.append(col_temp)
    cols_mid = np.vstack(cols_mid)
    colN = np.tile(np.hstack((Ocoln, Inxn)), (1, N))
    res = np.vstack((col1, cols_mid, colN))
    return res

def get_a_row(N):
    Inxn = np.eye(N)
    row1 = np.hstack((np.tile(Inxn, (1, N)), np.zeros((N, N**2 * (N-1)))))
    rows_mid = []
    for row in range(1, N-1):
        row_temp = np.hstack((np.zeros((N, row * N**2)), np.tile(Inxn, (1, N)), np.zeros((N, N**3 - (row+1) * N**2))))
        rows_mid.append(row_temp)
    rows_mid = np.vstack(rows_mid)
    rowN = np.hstack((np.zeros((N, N**2 * (N-1))), np.tile(Inxn, (1, N))))
    res = np.vstack((row1, rows_mid, rowN))
    return res

def get_a_clue(N, clues):
    hold_m = np.zeros((len(clues)//2, N**3))
    for i in range(0, len(clues), 2):
        val = clues[i]
        pos = clues[i+1]
        hold_m[i//2, N*pos - N + val] = 1
    return hold_m

def arrange_clues(size_of_puzzle, raw_clues):
    clues = []
    for i, clue in enumerate(raw_clues):
        if clue > 0:
            clues = clues + [(i + 1) % size_of_puzzle, i//size_of_puzzle]
    return clues

def make_a(size_of_puzzle, clues):
    a_clue = get_a_clue(size_of_puzzle, clues)
    a_cell = get_a_cell(size_of_puzzle)
    a_row = get_a_row(size_of_puzzle)
    a_col = get_a_col(size_of_puzzle)
    a = np.vstack((a_row, a_col, a_cell, a_clue))
    return a

def decoded_matrix(size_of_puzzle, clues):
    hold_m = np.zeros((size_of_puzzle, size_of_puzzle))
    for i in range(0, len(clues), 2):
        val = clues[i]
        pos = clues[i+1]
        row_num = pos // size_of_puzzle
        col_num = pos % size_of_puzzle
        hold_m[row_num, col_num] = val
    return hold_m

def sudoku_solver(size_of_puzzle, clues):
    clues = arrange_clues(size_of_puzzle, clues)
    print(clues)
    decoded = decoded_matrix(size_of_puzzle, clues)
    print(decoded)
    a = make_a(size_of_puzzle, clues)
    return a 