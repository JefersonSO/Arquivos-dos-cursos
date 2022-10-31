'''Conversor de dinheiro'''

moeda = str(input('Digite a moeda US$/EUR/R$: '))
valor = float(input('Digite o valor: '))
conversao = str(input('digite a moeda para qual deseja fazer a conversão: '))
if 'US$' in moeda and 'R$'in conversao :
    print(f'Resultado: R$ {valor*5.32:.2f}')
elif 'R$' in moeda and 'US$'in conversao:
    print(f'Resultado: US$ { (valor * 19 / 100):.2f}')
elif 'EUR' in moeda and 'R$'in conversao:
    print(f'Resultado: R$ { (valor *5.43):.2f}')
elif 'R$' in moeda and 'EUR'in conversao:
    print(f'Resultado: EUR { (valor * 18 / 100 ):.2f}')
elif 'EUR' in moeda and 'US$'in conversao:
    print(f'Resultado: US$ { (valor * 5.01):.2f}')
elif 'US$' in moeda and 'EUR'in conversao:
    print(f'Resultado: EUR { (valor * 99.1 / 100 ):.2f}')
else:
    print('opção invalida')

