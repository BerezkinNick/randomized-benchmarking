"""Подпрограмма для вывода обратной операции"""

from gates import *

str_cl1 = 'I'
str_cl2 = '(X ⋅ X)'
str_cl3 = '(X ⋅ X ⋅ Z ⋅ Z)'
str_cl4 = '(Z ⋅ Z)'

str_cl5 = 'X'
str_cl6 = '(Z ⋅ Z ⋅ X ⋅ Z ⋅ Z)'
str_cl7 = '(Z ⋅ X ⋅ Z ⋅ Z ⋅ Z)'
str_cl8 = '(Z ⋅ Z ⋅ Z ⋅ X ⋅ Z)'
str_cl9 = 'Z'
str_cl10 = '(Z ⋅ Z ⋅ Z)'

str_cl11 = '(X ⋅ Z)'
str_cl12 = '(Z ⋅ X)'
str_cl13 = '(X ⋅ Z ⋅ Z ⋅ Z)'
str_cl14 = '(Z ⋅ X ⋅ Z ⋅ Z)'
str_cl15 = '(Z ⋅ Z ⋅ X ⋅ Z)'
str_cl16 = '(Z ⋅ Z ⋅ Z ⋅ X)'
str_cl17 = '(Z ⋅ Z ⋅ X ⋅ Z ⋅ Z ⋅ Z)'
str_cl18 = '(Z ⋅ Z ⋅ Z ⋅ X ⋅ Z ⋅ Z)'

str_cl19 ='( X ⋅ X ⋅ Z)'
str_cl20 = '(X ⋅ Z ⋅ Z)'
str_cl21 = '(Z ⋅ X ⋅ X)'
str_cl22 = '(Z ⋅ X ⋅ Z)'
str_cl23 = '(Z ⋅ Z ⋅ X)'
str_cl24 = '(Z ⋅ Z ⋅ Z ⋅ X ⋅ Z ⋅ Z ⋅ Z)'

str_cl = [str_cl1, str_cl2, str_cl3, str_cl4, str_cl5, str_cl6, str_cl7, str_cl8, str_cl9, str_cl10, str_cl11, str_cl12, str_cl13, str_cl14, str_cl15, str_cl16, str_cl17, str_cl18, str_cl19, str_cl20, str_cl21, str_cl22, str_cl23, str_cl24]

str_H = 'i' + str_cl22
str_SPh = '(2^(-1/2))(1 + i)Z'
str_CZ = 'CZ'
str_S1 = '(-1)' + str_cl14
str_S2 = str_cl14 + ' ⋅ '+ str_cl14
str_CNOT = '(' + 'I ⊗ ' + str_H + ')' + ' ⋅ ' + str_CZ + ' ⋅ ' + '(' + 'I ⊗ ' + str_H + ')'
str_SWAP =  '(' + str_H + ' ⊗ ' + 'I' +  ')'  + ' ⋅ ' + str_CZ + ' ⋅ '  +  '(' + str_H + ' ⊗ ' + str_H +  ')' + ' ⋅ ' + str_CZ + ' ⋅ ' +  '(' + str_H + ' ⊗ ' + str_H +  ')' + ' ⋅ ' + str_CZ + ' ⋅ ' +  '(' + str_H + ' ⊗ ' + 'I' +  ')'
str_iSWAP = '(' + 'I ⊗ ' + str_H + ')' + ' ⋅ ' + str_CNOT +  ' ⋅ ' +  '(' + 'I ⊗ ' + str_H + ')' +  ' ⋅ ' +  '(' + str_SPh + ' ⊗ ' + str_SPh +  ')'  + ' ⋅ ' + str_SWAP
str_S = ['I', str_S1, str_S2]

str_gl = []

for i in range(24):
    for j in range(24):
        
        str_W1 = str_cl[i] +"⊗" + str_cl[j]
        str_gl.append(str_W1)
        
        str_W2 = str_SWAP + ' ⋅ '+ '(' + str_cl[i] +"⊗" + str_cl[j] + ')'
        str_gl.append(str_W1)

for i in range(3):
    for j in range(3):
        for k in range(24):
            for l in range(24):
                
                str_U1 = '(' + str_S[i] +" ⊗ " + str_S[j] + ')' + ' ⋅ '+  str_CNOT + ' ⋅ '+  '(' + str_cl[k] +" ⊗ " + str_cl[l] + ')'
                str_gl.append(str_U1)
                
                str_U2 = '(' + str_S[i] +" ⊗ " + str_S[j] + ')' + ' ⋅ '+  str_iSWAP + ' ⋅ '+  '(' + str_cl[k] +" ⊗ " + str_cl[l] + ')'
                str_gl.append(str_U2)


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
    E = cl[k] @ A
    print(coef(E[0][0]) +  str_cl[k])
    print('\n')

def show_2(k, A):
    E = gl[k] @ A
    print(coef(E[0][0]) + '[' + str_gl[k] + ']')
    print('\n')
