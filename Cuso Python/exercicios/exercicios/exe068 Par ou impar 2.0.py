from random import randint
while True:
    print('-=' * 20)
    resp = str(input('Par ou ímpar?: ').upper().strip()[0])
    print('-=' * 20)
    computador = randint(0, 10)
    n = int(input('Digite um numero: '))
    cont = 0
    soma = computador + n
    print('Deu par' if soma % 2 == 0 else 'Deu ímpar')
    if resp == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Voce perdeu!')
            break
    elif resp == 'I':
        if soma % 2 == 1:
            print('Voce venceu!')
            cont += 1
        else:
            print('Voce perdeu')
            break
    print(f'voce jogou{n}. o computador {computador}. deu {computador + n}')
    print('Vamos de novo...')
print(f'GAME OVER. voce venceu {cont} vez(es).')