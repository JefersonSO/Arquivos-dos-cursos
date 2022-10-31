#estrutura
todos = list()
jogador = dict()
gols = list()
while True:
    gols.clear()
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input(f'Quntas partidas {jogador["nome"]} jogou?'))
    for p in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {p+1}?: ')))
    jogador['gols'] = gols[:]
    todos.append(jogador.copy())
    while True:
        resp = str(input('continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('\033[2;31mErro! digite "S" ou "N"\033[m ')
    if resp == 'N':
        break
#mostrar
print(f'{"cod":<15}', end=" ")
for k in jogador.keys():
    print(f'{k:<15} ', end='')
print()
print('=-='*30)
for j, v in enumerate(todos):
    print(f'{j:<15} {v["nome"]:<15} {v["partidas"]:<15} {v["gols"]}')
print('=-='*30)
print()
while True:
    dados = int(input('Ver dados de qual jogador ? (999 para parar): '))
    if dados == 999:
        print('fim.')
        break
    if dados >= len(todos):
        print('\033[2;31mErro! não existe jogador com esse código na lista\033[m')
    else:
        print('-='*30)
        print(f'LEVANTAMENTO DE DADOS DO JOGADOR {todos[dados]["nome"]}\033[2;36m]')
        for d, g in enumerate(todos[dados]['gols']):
            print(f'na prtida {d+1} fez {g}')
        print('-=' * 30)

