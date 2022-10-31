tabela = ('Palmeiras', 'Corinthians', 'Fluminese', 'AtleticoPR', 'Flamengo',
          'Internacional', 'AtleticoMG', 'Bragantino','Santos', 'AmericaMG',
          'Botafogo', 'Goias', 'São Paulo', 'Ceara', 'Cuiaba', 'Avai', 'Curitiba',
          'Fortaleza', 'AtleticoG', 'Juventude')
for time in range(0,20):
    print(time+1,tabela[time])
print(f'Os 5 primeiro colocados sao {tabela[:5]}')
print(f'Os 4 ultimo colocados são {tabela[-4:]}')
print(f'Times em ordem alfabética {sorted(tabela)}')
print(f'O Flamengo aparece na posição {tabela.index("Flamengo")}º posição')
