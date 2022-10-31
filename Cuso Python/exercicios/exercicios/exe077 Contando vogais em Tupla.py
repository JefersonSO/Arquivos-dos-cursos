palavras = ( 'Deus', 'Infintas', 'Possibilidades', 'Eu', 'Superior')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end=' ')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')