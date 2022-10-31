num = int(input('Digite um numero: '))
print('''Escolha uma das bases para a conversão:
 [ 1 ] Converter para BINARIO
 [ 2 ] Converter para OCTAL
 [ 3 ] Converter para HEXAGONAL''')
opção = int(input('Sua opção'))
if opção == 1:
    print(' {} Convertido para BINARIO é igual á {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print( '{} Convertido para OCTAL é igual á {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print(' {} Convertido para HEXAGONAL é igual á {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida tente novamente')
