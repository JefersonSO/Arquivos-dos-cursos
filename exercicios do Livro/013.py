'''Elaborar um programa que realize a conversao entre metros, pes, polegadas e milhas'''
milimetro = 1
centimetro = 10*milimetro
metro = 100*centimetro
pe = 30.48*centimetro
milha = 1609.344*metro
polegada = 25.4*milimetro
v = float(input('Digite o valor : '))
esc1 = str(input('Escolha a medida [1] metro/ [2] pes / [3] milhas/ [4] polegadas : '))
esc2 = str(input('Converter  para  [1] metro/ [2] pes / [3] milhas/ [4] polegadas : '))
if '1' in esc1:
    if '2' in esc2:
        print(f'{v} metros são {(v*metro)/pe:.5f} pés')
    elif '3' in esc2:
        print(f'{v} metros são {(v*metro)/milha:.9f} milhas')
    elif '4' in esc2:
        print(f'{v} metros são {(v * metro) / polegada:.4f} polegadas')
if '2' in esc1:
    if '1' in esc2:
        print(f'{v} pés são {(v*pe)/metro:.5f} metros')
    elif '3' in esc2:
        print(f'{v} pés são {(v*pe)/milha:.9f} milhas')
    elif '4' in esc2:
        print(f'{v} pés são {(v*pe) / polegada:.4f} polegadas')
if '3' in esc1:
    if '1' in esc2:
        print(f'{v} milhas são {(v*milha)/polegada:.5f} metros')
    elif '2' in esc2:
        print(f'{v} milhas são {(v*milha)/pe:.9f} pés')
    elif '4' in esc2:
        print(f'{v} milhas são {(v*milha) / polegada:.4f} polegadas')
if '4' in esc1:
    if '1' in esc2:
        print(f'{v} polegadas são {polegada/(v*metro):.5f} metros')
    elif '3' in esc2:
        print(f'{v} polegadas são {(v*polegada)/milha:.9f} milhas')
    elif '2' in esc2:
        print(f'{v} polegadas são {(v*polegada) / pe:.4f} pés')
else:
    print('valor incorreto, fim.')
