import numpy as np
from main import *

"""l -длина последовательности, n - количество тестов"""
def test1(l, n):
    for i in range (n):
        V = random_sequence_1(l)
        m = find_inverse_1(V)
        A = c[m] @ V
        T = np.array([[1j]*4, [1j]*4])
        E = np.eye(2)
        p = 0
        for k in range(2):
            for l in range(2):
                T[0][p] = A[l][k]
                T[1][p] = E[l][k]
                p = p + 1  
        r = np.linalg.matrix_rank(T)
        if (r == 1):
            print('TRUE')
            print('\n')
        else:
            print('ERROR')
            print('\n')


def test2(l, n):
    for i in range (n):
        W = random_sequence_2(l)
        m = find_inverse_2(W)
        B = g[m] @ W
        T = np.array([[1j]*16, [1j]*16])
        E = np.eye(4)
        p = 0
        for k in range(4):
            for l in range(4):
                T[0][p] = B[l][k]
                T[1][p] = E[l][k]
                p = p + 1  
        r = np.linalg.matrix_rank(T)
        if (r == 1):
            print('TRUE')
            print('\n')
        else:
            print('ERROR')
            print('\n')

test1(1000, 100)
test2(1000, 100)
