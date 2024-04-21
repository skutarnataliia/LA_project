import numpy as np

def CheckColms(rawClues, sizeOfPuzzle):
    puzz = np.reshape(rawClues, (sizeOfPuzzle, sizeOfPuzzle))

    for j in range(sizeOfPuzzle):
        _, ind = np.unique(puzz[:, j], axis=0, return_index=True)
        duplicate_ind = np.setdiff1d(np.arange(puzz.shape[0]), ind)
        duplicate_value = puzz[duplicate_ind, j]

        if len(duplicate_value) < sizeOfPuzzle - 2:
            for p in range(sizeOfPuzzle):
                for b in range(len(duplicate_value)):
                    if puzz[p, j] == duplicate_value[b]:
                        puzz[p, j] = 0

    fixedColms = np.reshape(puzz, (sizeOfPuzzle, sizeOfPuzzle))
    return fixedColms

def CheckRows(rawClues, sizeOfPuzzle):
    puzz = np.reshape(rawClues, (sizeOfPuzzle, sizeOfPuzzle)).T

    for j in range(sizeOfPuzzle):
        _, ind = np.unique(puzz[:, j], axis=0, return_index=True)
        duplicate_ind = np.setdiff1d(np.arange(puzz.shape[0]), ind)
        duplicate_value = puzz[duplicate_ind, j]

        if len(duplicate_value) < sizeOfPuzzle - 2:
            for p in range(sizeOfPuzzle):
                for b in range(len(duplicate_value)):
                    if puzz[p, j] == duplicate_value[b]:
                        puzz[p, j] = 0

    fixedRows = np.reshape(puzz.T, (sizeOfPuzzle, sizeOfPuzzle))
    return fixedRows

def checker(correct, answers):
    count = 0
    for i in range(len(answers)):
        if correct[i] != answers[i]:
            count += 1
    return count

def wrapper(x, N):
    holder = np.zeros(N ** 2)
    x = np.reshape(x, (N, N ** 2))
    for i in range(len(holder)):
        idx = np.argmax(x[:, i])
        holder[i] = idx
    output = holder
    return output