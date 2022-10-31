my_list = []
maior = menor = 0
for v in range(0,5):
    n = int(input('digite um numero: '))
    my_list.append(n)
    if v == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Os Valores digitados foram: {my_list}')
print(f'O maior numero é {maior} e o menor numero é {menor}')