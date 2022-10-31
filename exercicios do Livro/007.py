'''A partir de cinco numeros reais, digitados pelo usuario, exibir o valor
da media considerando apenas os numeros que são maiores que zero e menores que mil.'''

n1 = float(input('Digite um nº: '))
n2 = float(input('Digite um nº: '))
n3 = float(input('Digite um nº: '))
n4 = float(input('Digite um nº: '))
n5 = float(input('Digite um nº: '))
media = 0

if n1 <= 0 or n1 >= 1000:
   media = (n2 + n3 + n4 + n5) / 4
elif n2 <= 0 or n1 >= 1000:
   media = (n1 + n3 + n4 + n5) / 4
elif n3 <= 0 or n1 >= 1000:
   media = (n1 + n2 + n4 + n5) / 4
elif n4 <= 0 or n1 >= 1000:
   media = (n1 + n2 + n3 + n5) / 4
elif n5 <= 0 or n1 >= 1000:
   media = (n1 + n2 + n3 + n4) / 4
else:
   media = (n2 + n3 + n4 + n5) / 4
print(media)
