import numpy as np
import random

from gates import *
from output import *

def random_sequence_1(l):
    """Генерация случайной последовательности длины l-1 для одного кубита"""
    r = random.randint(0, 23)
    V = c[r]
    for k in range(l-1):
        i = random.randint(0, 23)
        V = c[i] @ V
    return V
    

def random_sequence_2(l):
    """Генерация случайной последовательности длины l-1 для двух кубитов"""
    r = random.randint(0, 11519)
    W = g[r]
    for k in range(l-1):
        i = random.randint(0, 11519)
        W = g[i] @ W
    return W


def find_inverse_1(V):
    """Нахождение обратной операции для одного кубита"""
    q = 0
    R1 = np.linalg.inv(V)
    for i in range (len(c)):
        F = np.array([[1j]*4, [1j]*4])
        p = 0
        for k in range(2):
            for l in range(2):
                F[0][p] = c[i][l][k]
                F[1][p] = R1[l][k]
                p = p + 1  
        r = np.linalg.matrix_rank(F)
        if (r == 1):
            show_1(i, V)
            q = i
    return q


def find_inverse_2(W):
    """Нахождение обратной операции для двух кубитов"""
    q = 0
    R2 = np.linalg.inv(W)
    for i in range (len(g)):
        D = np.array([[1j]*16, [1j]*16])
        p = 0
        for k in range(4):
            for l in range(4):
                D[0][p] = g[i][l][k]
                D[1][p] = R2[l][k]
                p = p + 1  
        r = np.linalg.matrix_rank(D)
        if (r == 1):
            show_2(i, W)
            q = i
    return q

"""for t in range(4):
    V = random_sequence_1(1000)
    find_inverse_1(V)
    print('\n')

for t in range(4):
    W = random_sequence_2(1000)
    find_inverse_2(W)
    print('\n')"""

