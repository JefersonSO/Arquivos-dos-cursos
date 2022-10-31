'''Elaborar um programa que realize a  resolução de uma equação do 2º
grau utilizando, para isso, a formula de Báskara. '''
a = int(input('valor "a" '))
b = int(input('valor "b" '))
c = int(input('valor "c" '))

print(f'{a}x²{b}x{c}=0')
delta = (b**2) -4 * a * c
x1 = (-b + (delta**0.5)) / (2*a)
x2 = (-b - (delta**0.5)) / (2*a)
print(delta)
print(x1, x2)