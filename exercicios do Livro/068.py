'''Dada uma sequencia de 5 numeros inteiros digitados pelo
usuario, determinar e exibir a media.'''

soma = cont = 0

numeros = list()
while cont < 5:
    cont += 1
    num = int(input('Digite o {cont}º numero: '))
    numeros.append(num)
    soma += num

print(f'Foi digitado os seguintes numeros: {numeros} e a media é {soma / 5}')