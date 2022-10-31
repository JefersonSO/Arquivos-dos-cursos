from random import randint
from time import sleep
print('-='*25)
print(f'{"SORTEIO MEGA SENA":^50}')
print('-='*25)
my_list = []
list_temp = []

Qsort = int(input('Quantos jogos sortear?: '))
tot = 0
while tot <= Qsort:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in list_temp:
            list_temp.append(num)
            cont += 1
        if cont >= 6:
            break
    list_temp.sort()
    my_list.append(list_temp[:])
    list_temp.clear()
    tot += 1
print('=-'*3, f'SORTEANDO {Qsort} JOGOS','-='*3)
for i, l in enumerate(my_list):
    print(f'Jogo {i+1}: {l} ')
    sleep(1)
print('BOA SORTE!')