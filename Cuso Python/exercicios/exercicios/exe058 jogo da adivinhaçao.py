from random import randint
computador = randint(1, 10)
cont = 1
jogador = int(input('Pensei em um numero de 0 a 10, consegue adivinhar ?: '))
while jogador != computador:
    if jogador > computador:
        jogador = int(input('menos... tenta denovo'))
    if jogador < computador:
        jogador = int(input('mais...tenta denovo'))
    cont += 1
print('Voce acertou! o numero que eu pensei foi {}, voce precisou de {} tentativas'.format(computador, cont))
