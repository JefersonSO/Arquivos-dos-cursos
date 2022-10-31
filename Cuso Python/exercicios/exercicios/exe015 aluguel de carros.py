D = int(input('Quantos dia alugados? '))
km= (float(input('Quantos km rodados? ')))
pago = (D * 60)+(km * 0.15)
print('Total a pagar é de R$:{:.2f}' .format(pago))