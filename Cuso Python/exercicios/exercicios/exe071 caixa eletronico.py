print('-='*32)
print('{:^30}' .format('Banco CEV'))
print('-='*32)
valor = int(input('Quanto voce quer sacar? R$ '))
#o caixa possui cédulas de R$50, R$20, R$10 e R$1.
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f' total de {totced} cédulas de {ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-='*30)
print('Obrigado volte sempre!')

#codigo simplificado encontrado na internet

#valorSaque = int(input('Valor do saque: R$ '))
#print('-' * 40)
#for nota in [50, 20, 10, 1]:
 #   quantidade = valorSaque // nota
  #  valorSaque = valorSaque % nota
   # if quantidade > 0:
    #    print(f'{quantidade} notas de R$ {nota}')
