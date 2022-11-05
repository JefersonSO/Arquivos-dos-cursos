'''Elaborar um programa que calcule e mostre os  6 primeiros numeros da
sequencia de Fibonacci, ou seja 1,2,3,5,8 e 13.'''

t1 = 0
t2 = 1
t3 = 0
for c in range(3,9):
   t3 = t1 + t2
   print(t3)
   t1 = t2
   t2 = t3
