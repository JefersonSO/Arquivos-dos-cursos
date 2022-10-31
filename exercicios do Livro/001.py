'''Criar um programa que receba quatro numeros inteiros e exiba o menor deles'''

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
if (n1 < n2) and (n1 < n3) and (n1 < n4):
    print(f'O menor numero é {n1}')
elif (n2 < n1) and (n2 < n3) and (n2 < n4):
    print(f'O menor numero é {n2}')
elif (n3 < n1) and (n3 < n2) and (n3 < n4):
    print(f'O menor numero é {n3}')
else:
    print(f'O menor numero é {n4}')