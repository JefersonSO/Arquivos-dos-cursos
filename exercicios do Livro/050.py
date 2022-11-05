'''Considerando um numero inteiro ímpar, digitado pelo usuario,
exiba na tela um diamante(usando o numero 9) , por exemplo, se o usuario digitou nove,
 devemos obter a seguinte saida:'''

# Com For
soma = 0
n = int(input('Digite um nº ímpar: '))
for c1 in range(0, n+1):
    if c1 % 2 == 1:
        soma += 1
        print('{:{align}{width}}'.format('*'*c1,align='^', width=n))

for c2 in range(n+1, 0, -1):
    if c2 % 2 == 1:
        soma += 1
        print('{:{align}{width}}'.format('*'*c2,align='^', width=n))

#Com While
cont = 0
n = int(input('Digite um nº ímpar: '))
while True:
    cont += 1
    if cont % 2 == 1:
        print('{:{align}{width}}'.format('*'*cont,align='^', width=n))
        if cont == n:
           while cont != 0:
               cont -= 1
               if cont % 2 == 1:
                   print('{:{align}{width}}'.format('*'*cont,align='^', width=n))
    if cont == 0:
        break