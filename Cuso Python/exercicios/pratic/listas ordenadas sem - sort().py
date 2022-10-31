valores = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
       valores.append(n)
       print('valor adicionado ao final da lista')

    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionadao na posição {pos}')
                break
            pos += 1
print('lem é', len(valores)-1)
print(valores)


