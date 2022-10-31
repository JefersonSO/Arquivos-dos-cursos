'''Elabore uma rotina que,  a partir de um numero real digitado
pelo usuario, mostre o seu valor absoluto.  '''

n = float(input())
num = n
passo = 0

while True:
    if n > 0:
       n = n - 1
       passo += 1
    elif n <= 0:
        n = n + 1
        passo += 1
    if n == 0:
       break
print(f'O valor absoluto de {num} é {passo}')