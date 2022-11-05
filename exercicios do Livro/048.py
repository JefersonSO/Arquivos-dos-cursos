'''Criar uma rotina que mostre a somatoria dos 10 primeiros numeros
valora da Sequncia de Fibonacci.'''
soma = 0
t1 = 0
t2 = 1
t3 = 0
for c in range(3,13):
   t3 = t1 + t2
   print(t3)
   t1 = t2
   t2 = t3
   soma += t3

print(f'a somatoria dos 10 primeiros numeros da Sequncia de Fibonacci é {soma}')
