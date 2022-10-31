'''A partir de dois numeros inteiros digitados pelo usuario escrever uma rotina
 que mostre a media dos valores inteiros contidos no intervalo entre esses dois numeros.'''

n1 = int(input('n1º: '))
n2 = int(input('n2º '))
cont = 0
soma = 0

for c in range(n1, n2+1):
    if c > n1 and c < n2:
       cont += 1
       soma += c

media = soma / cont
print(f'A média entre esses dois numeros é {media} ')