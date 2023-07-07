"""Подпрограмма для вывода обратной операции"""

from gates import *

str_c1 = 'I'
str_c2 = '(X ⋅ X)'
str_c3 = '(X ⋅ X ⋅ Z ⋅ Z)'
str_c4 = '(Z ⋅ Z)'

str_c5 = 'X'
str_c6 = '(Z ⋅ Z ⋅ X ⋅ Z ⋅ Z)'
str_c7 = '(Z ⋅ X ⋅ Z ⋅ Z ⋅ Z)'
str_c8 = '(Z ⋅ Z ⋅ Z ⋅ X ⋅ Z)'
str_c9 = 'Z'
str_c10 = '(Z ⋅ Z ⋅ Z)'

str_c11 = '(X ⋅ Z)'
str_c12 = '(Z ⋅ X)'
str_c13 = '(X ⋅ Z ⋅ Z ⋅ Z)'
str_c14 = '(Z ⋅ X ⋅ Z ⋅ Z)'
str_c15 = '(Z ⋅ Z ⋅ X ⋅ Z)'
str_c16 = '(Z ⋅ Z ⋅ Z ⋅ X)'
str_c17 = '(Z ⋅ Z ⋅ X ⋅ Z ⋅ Z ⋅ Z)'
str_c18 = '(Z ⋅ Z ⋅ Z ⋅ X ⋅ Z ⋅ Z)'

str_c19 ='( X ⋅ X ⋅ Z)'
str_c20 = '(X ⋅ Z ⋅ Z)'
str_c21 = '(Z ⋅ X ⋅ X)'
str_c22 = '(Z ⋅ X ⋅ Z)'
str_c23 = '(Z ⋅ Z ⋅ X)'
str_c24 = '(Z ⋅ Z ⋅ Z ⋅ X ⋅ Z ⋅ Z ⋅ Z)'

str_c = [str_c1, str_c2, str_c3, str_c4, str_c5, str_c6, str_c7, str_c8, str_c9, str_c10, str_c11, str_c12, str_c13, str_c14, str_c15, str_c16, str_c17, str_c18, str_c19, str_c20, str_c21, str_c22, str_c23, str_c24]

str_H = 'i' + str_c22
str_SPh = '(2^(-1/2))(1 + i)Z'
str_CZ = 'CZ'
str_S1 = '(-1)' + str_c14
str_S2 = str_c14 + ' ⋅ '+ str_c14
str_CNOT = '(' + 'I ⊗ ' + str_H + ')' + ' ⋅ ' + str_CZ + ' ⋅ ' + '(' + 'I ⊗ ' + str_H + ')'
str_SWAP =  '(' + str_H + ' ⊗ ' + 'I' +  ')'  + ' ⋅ ' + str_CZ + ' ⋅ '  +  '(' + str_H + ' ⊗ ' + str_H +  ')' + ' ⋅ ' + str_CZ + ' ⋅ ' +  '(' + str_H + ' ⊗ ' + str_H +  ')' + ' ⋅ ' + str_CZ + ' ⋅ ' +  '(' + str_H + ' ⊗ ' + 'I' +  ')'
str_iSWAP = '(' + 'I ⊗ ' + str_H + ')' + ' ⋅ ' + str_CNOT +  ' ⋅ ' +  '(' + 'I ⊗ ' + str_H + ')' +  ' ⋅ ' +  '(' + str_SPh + ' ⊗ ' + str_SPh +  ')'  + ' ⋅ ' + str_SWAP
str_S = ['I', str_S1, str_S2]

str_g = []

for i in range(24):
    for j in range(24):
        
        str_W1 = str_c[i] +" ⊗ " + str_c[j]
        str_g.append(str_W1)
        
        str_W2 = str_SWAP + ' ⋅ '+ '(' + str_c[i] +" ⊗ " + str_c[j] + ')'
        str_g.append(str_W1)

for i in range(3):
    for j in range(3):
        for k in range(24):
            for l in range(24):
                
                str_U1 = '(' + str_S[i] +" ⊗ " + str_S[j] + ')' + ' ⋅ '+  str_CNOT + ' ⋅ '+  '(' + str_c[k] +" ⊗ " + str_c[l] + ')'
                str_g.append(str_U1)
                
                str_U2 = '(' + str_S[i] +" ⊗ " + str_S[j] + ')' + ' ⋅ '+  str_iSWAP + ' ⋅ '+  '(' + str_c[k] +" ⊗ " + str_c[l] + ')'
                str_g.append(str_U2)


def coef(A):
    if (np.round(A, 1) == 1):
        return('')
    
    if (np.round(A, 1) == -1):
        return('-1')
    
    if (np.round(A, 1) == 1j):
        return('i')
    
    if (np.round(A, 1) == -1j):
        return('-i')
    
    if (np.round(A, 1) == 0.7 + 0.7j):
        return('(2^(-1/2))(1 + i)')
    
    if (np.round(A, 1) == 0.7 - 0.7j):
        return('(2^(-1/2))(1 - i)')
    
    if (np.round(A, 1) == -0.7 + 0.7j):
        return('(2^(-1/2))(-1 + i)')
    
    if (np.round(A, 1) == -0.7 - 0.7j):
        return('(2^(-1/2))(-1 - i)')

def show_1(k, A):
    E = c[k] @ A
    print(coef(E[0][0]) +  str_c[k])
    print('\n')

def show_2(k, A):
    E = g[k] @ A
    print(coef(E[0][0]) + '[' + str_g[k] + ']')
    print('\n')
