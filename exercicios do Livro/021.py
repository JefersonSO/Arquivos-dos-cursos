'''Entre 4 valores digitados pelo usuario mostrar a diferença entre o maior e menor numero,'''
maior = 0
menor = 0

for c in range(1, 5):
    n = int(input())
    if maior == 0 and menor == 0:
       maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'O menor valor é {menor} e o maior é {maior} e a diferença entre eles é {maior-menor}')
