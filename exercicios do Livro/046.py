'''Mostrar a quantidade de numeros multiplos de 7 que estão
em um intervalo fornecido pelo usuario.'''

n1 = int(input('Digite o inicio: '))
n2 = int(input('Digite o fim: '))
print('Os multiplos de 7 nesse intervalo são: \nM(7) = ', end='')
if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux
for c in range(n1, n2):
    print(c*7, end=' ')