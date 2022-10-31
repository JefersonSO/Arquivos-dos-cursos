valor = float(input('Qual é o valor da casa?: '))
salario = float(input('Qual a sua renda>; '))
anos = int(input('Em quantos anos deseja pagar?: '))
p = valor / (anos * 12)
c = salario * 30 / 100
if p <= c:
    print('A prestaçao sera de {:.2f} aprovado !' .format(p))
else:
    print(' A prestaçao sera de {:.2f} Não aprovado'.format(p))
