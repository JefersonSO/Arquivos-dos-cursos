'''Em uma classe há 10 alunos, cada um dos quais realizou 3 provas
com pesos distintos, sendo que a primeira prova posssui peso 3,
 a segunada possui peso 4 e a terceira, peso 3. Apos o lançamento
das notas, calcular a media para cada um dos alunos.'''

classe = list()
todas_notas = list()
media = 0
todas_as_medias = list()

#os 10 alunos
for c in range(0,10):
    classe.append(c)

#definindo as notas de cada aluno
for c in classe:
    print(f'Digte as 3 notas do {c+1}º aluno :')
    notas = [],[],[]
    for c2 in range(0,3):
        num = float(input(f'n{c2+1}:'))
        notas[c2].append(num)

#peso das notas
        if c2 == 1:
           media += num*4
        else:
            media += num*3
    todas_notas.append(notas)
    todas_as_medias.append(media / 10)
    media = 0

#imprimindo o resultado
for c in classe:
    print(f'O {c+1}º aluno tirou as notas{todas_notas[c]} e a sua media é {todas_as_medias[c]} ')