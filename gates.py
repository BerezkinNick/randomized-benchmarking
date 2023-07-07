import numpy as np

def tens(A, B):
    """Тензорное произведение"""

    c = 1j*np.eye(4)
    
    for i in range(2):
        for j in range(2):
            c[i][j] = A[0][0]*B[i][j]
        
    for i in range(2, 4):
        for j in range(2):
            c[i][j] = A[1][0]*B[i-2][j]
        
    for i in range(2):
        for j in range(2, 4):
            c[i][j] = A[0][1]*B[i][j-2]
        
    for i in range(2, 4):
        for j in range(2, 4):
            c[i][j] = A[1][1]*B[i-2][j-2]
    return(c)

#базовые гейты
I = np.array([[1, 0], [0, 1]])
X = 1/np.sqrt(2)*np.array([[1, -1j], [-1j, 1]])
Z = 1/np.sqrt(2)*np.array([[1-1j, 0], [0, 1+1j]])
CZ = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])

c = [X]*24

"""Группа Клиффорда для одного кубита"""
#Группа Паули
c[0] = I
c[1] = X @ X
c[2] = X @ X @ Z @ Z
c[3] = Z @ Z

#Вращения на pi/2
c[4] = X
c[5] = Z @ Z @ X @ Z @ Z
c[6] = Z @ X @ Z @ Z @ Z
c[7] = Z @ Z @ Z @ X @ Z
c[8] = Z
c[9] = Z @ Z @ Z

#Вращения на 2*pi/3
c[10] = X @ Z
c[11] = Z @ X
c[12] = X @ Z @ Z @ Z
c[13] = Z @ X @ Z @ Z
c[14] = Z @ Z @ X @ Z
c[15] = Z @ Z @ Z @ X
c[16] = Z @ Z @ X @ Z @ Z @ Z
c[17] = Z @ Z @ Z @ X @ Z @ Z

#Адамары
c[18] = X @ X @ Z
c[19] = X @ Z @ Z
c[20] = Z @ X @ X
c[21] = Z @ X @ Z
c[22] = Z @ Z @ X
c[23] = Z @ Z @ Z @ X @ Z @ Z @ Z


H = 1j * Z @ X @ Z #Гейт Адамара
SPh = 2**(-1/2) * (1 + 1j) * Z #Гейт SPhase

#Циклические перестановки
S1 = (-1) * Z @ X @ Z @ Z
S2 = S1 @ S1
S = [I, S1, S2]

#Двухкубитные гейты
CNOT = tens(I, H) @ CZ @ tens(I, H)
SWAP = tens(H, I) @ CZ @ tens(H, H) @ CZ @ tens(H, H) @ CZ @ tens(H, I)
iSWAP = tens(I, H) @ CNOT @ tens(I, H) @ tens(SPh, SPh) @ SWAP

"""Группа Клиффорда для двух кубитов"""
g = []

for i in range(24):
    for j in range(24):
        
        W1 = tens(c[i], c[j]) #класс Cl(||)
        g.append(W1)
        
        W2 = SWAP @ tens(c[i], c[j]) #класс Cl(SWAP)
        g.append(W2)

for i in range(3):
    for j in range(3):
        for k in range(24):
            for l in range(24):
                
                U1 = tens(S[i], S[j]) @ CNOT @ tens(c[k], c[l]) #класс Cl(CNOT)
                g.append(U1)
                
                U2 = tens(S[i], S[j]) @ iSWAP @ tens(c[k], c[l]) #класс Cl(iSWAP)
                g.append(U2)

