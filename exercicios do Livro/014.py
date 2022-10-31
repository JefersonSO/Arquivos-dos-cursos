'''Apartir de um valor digitado pelo usuario e o respectivo prefixo
mostrar a representação do valor nos demais prefixos.'''

#prefixos K(kilo) M(mega) G(giga) T(terra)

v = float(input())
K = v**3
M = v**6
G = v**9
T = v**12
prefixo = str(input('escolha K/M/G/T: ')).upper()

if 'K' in prefixo :
    print(f'{M:.6f} M')
    print(f'{G:.9f} G')
    print(f'{T:.12f} T')
elif 'M' in prefixo:
    print(f'{K:.6f} K')
    print(f'{G:.9f} G')
    print(f'{T:.12f} T')
elif 'G' in prefixo:
    print(f'{K:.6f} K')
    print(f'{M:.6f} M')
    print(f'{T:.12f} T')
elif 'T' in prefixo:
    print(f'{K:.6f} K')
    print(f'{M:.6f} M')
    print(f'{G:.9f} G')
else:
    print('Eroo!')