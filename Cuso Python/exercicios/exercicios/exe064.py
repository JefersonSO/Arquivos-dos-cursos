cont = n = soma = 0
n = int(input('Digite um numrero [999 para parar: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numrero [999 para parar: '))
print(' digitou {} A soma dos nº foi {}'.format(cont, soma))
print('fim.')


