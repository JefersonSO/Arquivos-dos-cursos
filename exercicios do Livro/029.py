'''Escreva um programa que realize a exibição, em ordem decrescente,
 dos números inteiros entre 0 e 200 e que tambem sejam multiplos de 5.'''
print()
print('Multiplos de 5 entre 0 e 200 em ordem decrescente M(5) = ')
for c in range(200, 0, -5):
      print(c*5, end=' ')
