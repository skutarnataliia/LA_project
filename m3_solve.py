import numpy as np
import cvxpy
from math import sqrt
from m3_func import *
from m3_check import *

def L1SudokuSolving(orginClues, guesses, iterCount):
    sizeOfPuzzle = int(sqrt(len(orginClues)))
    rawGuesses = guesses[:]
    guesses = arrange_clues(sizeOfPuzzle, guesses)
    holder = [0] * (sizeOfPuzzle ** 2)

    A = make_a(sizeOfPuzzle, rawGuesses)

    b = np.ones((A.shape[0], 1))

    m, n = A.shape

    x = cvxpy.Variable((n, 1))
    objective = cvxpy.Minimize(cvxpy.norm(x, 1))
    constraints = [A * x == b]
    problem = cvxpy.Problem(objective, constraints)
    problem.solve()

    iterationThresh = 10

    if iterCount >= iterationThresh:
        wraped = wrapper(x.value, sizeOfPuzzle)
        sol = wraped
    else:
        wraped = wrapper(x.value, sizeOfPuzzle)

        x = np.reshape(x.value, (sizeOfPuzzle, sizeOfPuzzle ** 2))

        fixedRows = CheckRows(holder, sizeOfPuzzle)
        fixedColms = CheckColms(holder, sizeOfPuzzle)
        for u in range(len(fixedRows)):
            for v in range(4):
                if fixedRows[u][v] == 0 or fixedColms[u][v] == 0:
                    holder[4*u+v] = 0

                if orginClues[4*u+v] != 0:
                    holder[4*u+v] = orginClues[4*u+v]
                

    sol = holder
    return sol