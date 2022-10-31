print('\033[0;36m', ' -=-' * 4, 'Lojas JefSon',' -=-' * 4 )
print(' ')
valor = float(input('Digite o valor da compra: '))
print('''Opções de compra:
[1] À vista no dinheiro/cheque 10% de desconto
[2] À vista no cartão 5% de desconto
[3] Em ate 2x no cartão: preço formal
[4] Em 3x ou mnais no cartão: 20% de juros''')
opção =int(input('Escolha uma opção:'))
if opção == 1:
   avista = valor - (valor * 10 / 100)
   print('{:.2f} à vista com 10% de desocnto fica {:.2f}'.format(valor, avista))
elif opção == 2:
    cartão = valor - (valor * 5 / 100)
    print('{:.2f} á vista no cartão fica {:.2f}'.format(valor, cartão))
elif opção == 3:
    dx = valor / 2
    print('{:.2f} em 2x no cartao 2x{:.2f}'.format(valor, dx))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    tx = valor / parcelas
    print('{:.2f} em {}x fica {}x{:.2f}'.format(valor, parcelas, parcelas, tx))
print(' ')
print(' -=-' * 11)
