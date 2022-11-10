'''Deseja-se determinar o numero de acertos de um aluno em uma prova em forma de testes.
 Aprova consta de 25 questoes, cada uma com alternativas identificadas por A,B,C,D e E.
 Para determinar os acertos, esta prova deverá ser comparada ao seguite gabarito:
 B,C,A,D,B,B,E,C,A,B,D,A,A,A,A,B,D,C,E,E,A,C,E,D,B.
.
'''

gabarito = ['B','C','A','D','B','B','E','C','A','B','D','A',
            'A','A','A','B','D','C','E','E','A','C','E','D','B']
prova = list()
acertos = 0
for c in range(0,25):
    nota = str(input(f'{c}º Nota: ')).upper()
    prova.append(nota)
    if nota == gabarito[c]:
        acertos += 1
print(f'Total de acertos {acertos}')
print(f'sua prova {prova}')
if prova == gabarito:
    print('Parabens você gabaritou!')

