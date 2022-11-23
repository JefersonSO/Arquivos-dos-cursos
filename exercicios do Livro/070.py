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
#Imprimindo o vetor
print()
for l in jogo:
     for c in l:
         if c % 2 == 0:
             print('x', end='  ')
         else:
             print('O', end='  ')

         if c == l[0] or c == l[1]:
              print('│',end='  ')
         if c == 3 or c  == 6:
            print()
            print('-'*15)




