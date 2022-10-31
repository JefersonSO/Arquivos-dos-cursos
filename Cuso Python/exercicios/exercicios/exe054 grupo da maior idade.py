from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8,):
    data = int(input('Data de nascimento:'))
    soma = date.today().year
    if (soma - data) > 18:
        totmaior += 1
        print('A data de nascimento da {}ºpessoa é {} ela tem {} anos e é de maior de idade '.format(c, data, soma - data))
    elif (soma - data) < 18:
        totmenor += 1
        print('A data de nascimento da {}ºpessoa é {} ela  tem {} anos e é de menor de idade'.format(c, data, soma - data))
print('Das {} pessoas {} são maior(es) de idade e {} são menor(es) de iadade'.format(c, totmaior , totmenor))