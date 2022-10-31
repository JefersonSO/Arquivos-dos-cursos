valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        print('Valor adicionado com sucesso...')
        valores.append(n)
    else:
       print('Valor duplicado! Não vou adicionar..,')

    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
valores.sort()
print(valores)