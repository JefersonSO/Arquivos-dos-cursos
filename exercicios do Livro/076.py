from random import randint

'''Considerando um vetor de 500 numeros inteiros, carregado
randomicamente com valores entre 1 e 1000, calcular e exibir
o valor da média dos elementos armazenados no vetor.'''


valores = list()
cont = soma = 0
while cont != 500:
    n = randint(1,1000)
    valores.append(n)
    cont += 1
    soma += n
media = soma / len(valores)
for c, num in enumerate(valores):
        print(num, end='')
        if c >= 0 and c < 499:
            print(',', end='')
        elif c == 499:
            print('.', end='')
print()
print(f'A média dos numeros sorteados é {media}')