'''Calcular a circunferência, a partir do raio(R) digitado pelo usuario.
O comprimento é obtido pela formula 2 x pi x R ((4/3) * pi * R3)'''
R = float(input('Digite o raio: '))
pi = 3.14159
comp = (4/3) * pi * R**3
print(f'O comprimento da circunferência é {comp:.3f}')
