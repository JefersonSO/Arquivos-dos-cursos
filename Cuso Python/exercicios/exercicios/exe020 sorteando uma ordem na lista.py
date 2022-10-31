import random
aluno1 = str(input('Nome do 1° aluno: '))
aluno2 = str(input('Nome do 2° aluno: '))
aluno3 = str(input('Nome do 3° aluno: '))
lista = [aluno1, aluno2, aluno3]
r = random.shuffle(lista)
print('A ordem dos alunos é {}')
print(lista)

