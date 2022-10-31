'''Determinada loja precisa digitar o nome  e o preço dos seus produtos.
Após cada produto digitado, deverá ser realizada uma pergunta se deseja digitar outro
produto. Caso o usuario responda "sim" , um novo produto será digitado, caso contrario,
 o programa deverá, antes de encerrar, exibir o nome do produto mais caro.'''

maior = 0
mais_caro = 0
while True:
    nomeP = str(input('Nome do produto: '))
    precoP = float(input('Preço do produto R$:'))
    if maior == 0:
        maior = precoP
    if precoP > maior:
        maior = precoP
        mais_caro = nomeP
    esc = str(input('Outro produto? S / N: ')).upper()
    if esc in 'S':
        continue
    else:
        print(f'O produto mais caro foi {mais_caro} R$ {maior}.')
        break