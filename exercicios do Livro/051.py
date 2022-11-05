'''Faça uma rotina que permita calcular o valor da associação em serie
de tres resistores R1, R2, R3, que srão digitados pelo usuario.
O programa ficara solicitando os valores de R1, R2 e R3 e exibindo
o resultado até que o usuario digite um valor para R1, R2 ou R3 igual a zero.
O valor da associação em serie de tres resistores será obtido pela formula:
 R = R1 + R2 + R3.'''

while True:
   R1 = int(input('R1: '))
   R2 = int(input('R2: '))
   R3 = int(input('R3: '))
   Result = R1 + R2 + R3
   print(f'R: {Result}')
   if R1 == 0 or R2 == 0 or R3 == 0:
       break



