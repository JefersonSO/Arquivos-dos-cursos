from random import randint
'''Desenvolver um programa que sorteie um numero aleatorio entre 0 e 500
e pergunte ao usuario qual é o "numero mágico". O programa devera indicar
 se a tentativa efetuada pelo usuario é maior ou menor que o numero magico
 e contar o numero de tentativas. O progama apenas deverá encerrar quando
 o usuario acertar o numero. Neste momento, também deverá mostrar uma mensagem, classificando o usuario como:
 
 - De 1 a 3 tentativas: muito sortudo;
 - De 4 a 6 tentativas: sortudo;
 - De 7 a 10 tentativas: normal;
 - 10 tentativas: tente novamente.'''

n = 0
tentativas = 0
n_sorteado = randint(0,500)
while n != n_sorteado:
    n = int(input('Chute um numero: '))
    tentativas += 1
    if n == n_sorteado:
        if tentativas >= 1 or n <= 3:
            print(f'nº tentativas {tentativas}. Muito Sortudo!')
        elif tentativas >= 4 or n <= 6:
            print(f'nº tentativas {tentativas}. Sortudo!')
        elif tentativas >= 7 or n <= 10:
            print(f'nº tentativas {tentativas}. Normal.')
        elif tentativas > 10:
            print(f'nº tentativas {tentativas}. Tente Novamente.')
        break
    else:
        print('Errou')

        if n < n_sorteado:
            print(f'{n}é menor que o nº Magico!')
        elif n > n_sorteado:
            print(f'{n}é maior que o nº Magico!')

print(f'O numero sorteado foi {n_sorteado}')