dados = dict()
listatemp = list()
dados['nome'] = str(input('Nome: '))
dados['partidas'] = int(input(f'Numero de partidas de {dados["nome"]} '))
for g in range(0, dados['partidas']):
    listatemp.append(int(input(f'  Quantos gols na partida {g}?: ')))
dados['gols'] = listatemp[:]
dados['somagols'] = sum(dados['gols'])
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
for k, v in enumerate(dados['gols']):
    print(f'    => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {dados["somagols"]}.')
