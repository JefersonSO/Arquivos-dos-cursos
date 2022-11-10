'''Considerando 5 numeros reais digitados pelo usuario e armazenados
em um vetor, exibir o valor da somatoria deles.'''

soma = 0
valores = list()
for c in range(1,6):
    valores.append(float(input(f'nº{c}: ')))
for c, v in enumerate(valores):
    soma += v
print(soma)
