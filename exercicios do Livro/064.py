
'''Um dado de jogo foi lançado 20 vezes. A partir dos resultados
 dos lançamentos, determinar o numero de ocorrencias de cada face.'''

dado = list()
from random import *
for vezes in range(0,20):
    dado.append(randint(1,6))
if 6 in dado:
   print(f'o numero 6 caiu {dado.count(6)}x' )
if 5 in dado:
   print(f'o numero 5 caiu {dado.count(6)}x' )
if 4 in dado:
   print(f'o numero 4 caiu {dado.count(6)}x' )
if 3 in dado:
   print(f'o numero 3 caiu {dado.count(6)}x' )
if 2 in dado:
   print(f'o numero 2 caiu {dado.count(6)}x' )
if 1 in dado:
   print(f'o numero 1 caiu {dado.count(6)}x' )

print(dado)