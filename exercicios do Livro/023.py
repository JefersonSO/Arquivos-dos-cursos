'''A area de um triangulo (A) é definida pela metade do produto entre
 a altura (H) pela base (B). escrever um programa que, a partir da altura e base calcuçe a aerea
 com valores reais maiores que zero    '''


H = float(input('Digite a altura: '))
B = float(input('Digite a base: '))
if H == 0 or B == 0:
    print('ERRO! zero não é divisivel')
A = (H*B) / 2
print(f'A area do triangulo é {A}')
print('nop')
