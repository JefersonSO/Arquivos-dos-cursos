valores = []
for n in range(0,5):
    v = int(input('Digite um valor : '))
    if n == 0 or v > valores[-1]:
        valores.append(v)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
               valores.insert(pos, v)
               print(f'Adicionado na posição {n}')
               break
            pos += 1
print(valores)