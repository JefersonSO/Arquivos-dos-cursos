from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
for j in range(1,5):
    jogo[j] = randint(1, 6)
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'Jogador {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(' == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'   {i+1}ºlugar jogador {v[0]} com {v[1]}')
    sleep(1)