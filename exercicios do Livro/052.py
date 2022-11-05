'''Faça uma rotina que permita calcular o valor da associação em paralelo
de dois resistores R1 e R2, que serão digitados pelo usuario e consistem
 em numeros reais positivos. O programa ficará solicitando os valores de
R1 e R2 e exibindo o resultado até que o usuario digite um valor para R1
ou R2 igual a zero. O valor da associação em paralelo de dois resistores
será obtido pela fórmula: R = R1 x R2 / (R1 + R2).'''

while True:
    R1 = float(input('R1: '))
    R2 = float(input('R2: '))
    Result = R1 * R2 / (R1 + R2)
    print(f'Resultado: {Result}')
    if R1 == 0 or R2 == 0:
        break