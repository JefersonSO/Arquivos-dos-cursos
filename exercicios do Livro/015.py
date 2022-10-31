'''Utilizando o exercicio anterior mostre agora o valor do prefixo escolhido'''
#prefixos K(kilo) M(mega) G(giga) T(terra)

v = float(input())
K = v**3
M = v**6
G = v**9
T = v**12
prefixo = str(input('escolha K/M/G/T: ')).upper()

if 'K' in prefixo :
    print(f'{K:.6f} K')
elif 'M' in prefixo:
    print(f'{M:.6f} M')
elif 'G' in prefixo:
    print(f'{G:.9f} G')

elif 'T' in prefixo:
    print(f'{T:.12f} T')
else:
    print('Eroo!')