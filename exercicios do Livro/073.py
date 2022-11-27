'''Representar em uma matriz e, em seguida, exibir na tela o seguinte
estado de um jogo da velha:
 O │ X │
-----------
   │ O │
-----------
 X │   │ O '''

cont = 0
A = list()
B = list()
for l in range(0,3):
    for c in range(0,3):
        B.append(' ')
    A.append(B[:])
    B.clear()
A[0][0] = A[1][1] = A[2][2] = 'O'
A[0][1] = A[2][0] = 'X'
print()
for l in range(0,3):
    for c in range(0,3):
        print(A[l][c], end='')
        if c == 0 or c == 1:
           print(' │',end=' ')

    print()
    if l == 0 or l == 1:
       print('-'*10)