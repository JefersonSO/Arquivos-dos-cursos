preço = float(input('valor Pc gamer R$ '))
avista = preço-(preço*10/100)
print('Pc gamer R${} pagamento a vista com 10% de desconto  R${:.2f} ' .format(preço, avista,))
parcelado = int(input('Quer parcelar? digite o numero de parcelas desejado: '))
total = preço/parcelado
print('podendo parcelar em até {:2}x  {:.2f} sem juros'.format(parcelado, total))