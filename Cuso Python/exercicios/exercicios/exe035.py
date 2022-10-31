r1 = float(input('primeiro seguimento'))
r2 = float(input('Segundo seguimento'))
r3 = float(input('terceiro seguimento'))
if r1 < r2 + r3  and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo')
else:
    print('Os seguimentos acima não podem formar um triangulo')