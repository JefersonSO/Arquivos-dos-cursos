'''Implemente o tradicional jogo da velha a partir de uma matriz 3 x 3,
sendo que a matriz deve representar os seguintes valores possiveis: O,X
e nulo(vazio).'''

#Titulo
print('-'*30)
print('      Jogo da velha       ')
print('-'*30)

#vetor 3x3
cont = 0
jogo = list()
posicoes = list()
for linha in range(0,3):
       for coluna in range(0,3):
           cont += 1
           posicoes.append(cont)
       jogo.append(posicoes[:])
       posicoes.clear()
posicoes.clear()
cont = 0
print('O primeiro a jogar é o "X".')
while True:
    print(jogo)
    #Imprimindo o vetor
    print()
    for l in jogo:
         for c, v in enumerate(l):
             print(v, end='  ')
             if c == 0 or c == 1:
                  print('│',end='  ')
             if c == 2:
                print()
                print('-'*13)
    cont += 1
    esc = int(input(f'vez do jogador {cont} na posiçao :'))
    if cont == 2:
        cont = 0
    for l in range(0,3):
        for c in range(0,3):
            if jogo[l][c] == esc:
                if cont == 1:
                   jogo[l][c] = '\033[0;34mX\033[m'
                else:
                    jogo[l][c] = '\033[0;31mO\033[m'


