''' Desenvolver uma rotina que apartir de um caractere e uma determinada
quantidade de linhas e colunas, todos fornecidos pelo usuario, realize a
repetição do respectivo caractere na quantidade de linhas e colunas que
foram digitadas. Por exemplo:

Entrada:
Linhas? 3
Colunas? 5
Caractere? X

Saida:
xxxxx
xxxxx
xxxxx '''


l = int(input('nº de Linhas: '))
c = int(input('nº de colunas: '))
caractere = str(input('Caractere: '))

for cont in range(0, l):
    print(f'{caractere*c}')
