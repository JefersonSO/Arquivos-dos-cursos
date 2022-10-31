import random

aluno1 = input(' Nome do primeiro aluno: ')
aluno2 = input(' Nome do segundo aluno: ')
aluno3 = input(' Nome do terceiro aluno: ')
aluno4 = input(' Nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
r = random.choice(lista)
print(' O aluno escolhido foi {} '.format(r))
