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

"""Группа Клиффорда для одного кубита"""
#Группа Паули
cl1 = I
cl2 = X @ X
cl3 = X @ X @ Z @ Z
cl4 = Z @ Z

#Вращения на pi/2
cl5 = X
cl6 = Z @ Z @ X @ Z @ Z
cl7 = Z @ X @ Z @ Z @ Z
cl8 = Z @ Z @ Z @ X @ Z
cl9 = Z
cl10 = Z @ Z @ Z

#Вращения на 2*pi/3
cl11 = X @ Z
cl12 = Z @ X
cl13 = X @ Z @ Z @ Z
cl14 = Z @ X @ Z @ Z
cl15 = Z @ Z @ X @ Z
cl16 = Z @ Z @ Z @ X
cl17 = Z @ Z @ X @ Z @ Z @ Z
cl18 = Z @ Z @ Z @ X @ Z @ Z

#Адамары
cl19 = X @ X @ Z
cl20 = X @ Z @ Z
cl21 = Z @ X @ X
cl22 = Z @ X @ Z
cl23 = Z @ Z @ X
cl24 = Z @ Z @ Z @ X @ Z @ Z @ Z

cl = [cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9, cl10, cl11, cl12, cl13, cl14, cl15, cl16, cl17, cl18, cl19, cl20, cl21, cl22, cl23, cl24]

H = 1j * Z @ X @ Z #Гейт Адамара
SPh = 2**(-1/2) * (1 + 1j) * Z #Гейт SPhase

S1 = (-1) * Z @ X @ Z @ Z #Циклические перестановки
S2 = S1 @ S1
S = [I, S1, S2]

#Двухкубитные гейты
CNOT = np.round(tens(I, H) @ CZ @ tens(I, H))
SWAP = np.round(tens(H, I) @ CZ @ tens(H, H) @ CZ @ tens(H, H) @ CZ @ tens(H, I))
iSWAP = np.round(tens(I, H) @ CNOT @ tens(I, H) @ tens(SPh, SPh) @ SWAP)

gl = []

for i in range(24):
    for j in range(24):
        
        W1 = tens(cl[i], cl[j])
        gl.append(W1)
        
        W2 = SWAP @ tens(cl[i], cl[j])
        gl.append(W2)

for i in range(3):
    for j in range(3):
        for k in range(24):
            for l in range(24):
                
                U1 = tens(S[i], S[j]) @ CNOT @ tens(cl[k], cl[l])
                gl.append(U1)
                
                U2 = tens(S[i], S[j]) @ iSWAP @ tens(cl[k], cl[l]) #iSWAP
                gl.append(U2)

