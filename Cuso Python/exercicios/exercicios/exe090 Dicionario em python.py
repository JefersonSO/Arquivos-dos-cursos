dadosA = dict()
dadosA['nome'] = str(input('Nome: '))
dadosA['media'] = float(input(f'media de {dadosA["nome"]}: '))
print('-='* 35)
if dadosA['media'] <= 7 and  dadosA['media'] > 5:
    dadosA['situacao'] =  'Recupração'
elif dadosA['media'] <= 5:
    dadosA['situacao'] =  'Reprovado'
else:
    dadosA['situacao'] = 'Aprovado!'
for k, v in dadosA.items():
    print(f' {k} é igual a {v}')