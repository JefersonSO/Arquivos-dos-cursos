maior = menor = cont = M1000 = soma = 0
barato = ' '
while True:
    print('-' * 20)
    produto = str(input('Nome do produto: ')).upper().strip()[0]
    preço = int(input('Digite o preço R$: '))
    print('-' * 20)
    soma += preço
    cont += 1
    if preço >= 1000:
        M1000 += 1
    if cont == 1 or menor < preço:
         menor = preço
         barato = produto
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar?: [S/N] ')).upper().strip()[0]
    if c == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O valor total foi {soma}. total de {M1000} itens no valor ou acima de R$ 1000  o menor valor digitado foi {produto} {menor}')