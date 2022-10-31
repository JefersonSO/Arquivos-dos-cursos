print('='*33)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('='*33)
produtos = ('lápis ', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.60,
            'Estojo', 25.00,
            'Transferido', 4.20,
            'Compasso',  9.99,
            'Mochila', 120.30,
            'Canetas', 22.30,
            'Livro', 34.90)
for c in range(0, len(produtos)):
    if c % 2 == 0:
       print(f'{produtos[c]:.<30}',end='')
    else:
       print(f'R$ {produtos[c]:>5}')
print('='*33)