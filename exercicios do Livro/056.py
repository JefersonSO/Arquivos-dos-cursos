'''Elaborar um programa que apresente a resolução do seguinte problema:
'Determinada loja precisa digitar o nome e o preço de 10 produtos.
Após a digitação dos 10 produtos o programa deverá, antes de encerrar,
exibir o nome do produto mais caro.'''

maior = 0
mais_caro = ''

for p in range(1,11):
    prod = str(input(f'Nome do {p}ºproduto: '))
    preco = float(input('preço R$: '))
    if maior == 0:
        maior = preco
    if maior > preco :

        mais_caro = prod

print(f'O produto mais caro é {mais_caro} R$ {maior}')