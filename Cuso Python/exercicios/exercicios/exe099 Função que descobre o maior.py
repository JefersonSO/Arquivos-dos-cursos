from time import sleep
def maior(*num):
    print('=-'*30)
    maior = 0
    tam = len(num)
    print('Analizando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.3)
    for c, n in enumerate(num):
        if c == 0:
            maior = n
        else:
            if n > maior:
               maior = n

    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior} ')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
