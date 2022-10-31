from random import randint
Qn = (randint(1,10), randint(1,10), randint(1,10),
randint(1,10))
print(f'Os numeros sorteados foram: {Qn}')
if 3 in Qn:
    print(f'vezes que o valor 3 na pos {Qn.index(3)+1}')
else:
    print('valor 3 nao encontrado')

print(f'Vezes em que o valor 9 aparece {Qn.count(9)} ')
print(f'numeros pares sao:', end='')
for c in Qn:
    if c % 2 == 0:
        print(c, end=',')


