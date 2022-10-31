print('\033[5;35m''-='*20)
print('Analisador de triangulos')
print('\033[3;35m''-='*20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Tereiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo.', end='')
    if r1 == r2 == r3:
        print('Esse triângulo é um EQUILATERO.')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é ESCALENO.')
    else:
        print('Esse triãngulo é ISÓCELES.')
else:
    print('Os seguimentos acima não podem formar um triângulo.')



