'''calcular a area e informar se é um retangulo ou quadrado'''

l = float(input('Base: '))
a = float(input('Altura: '))

if l == a :
    print(f'È um quadrado, sua area é {l * a}' )
else :
    print(f'È um retangulo, sua area é {l * a}' )
