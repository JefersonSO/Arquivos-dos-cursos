salario = float(input('Qual o seu salario atual?R$ '))
if salario <= 1.200:
  novo = + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O sslario atualisado é/;R$ {}' .format(novo))


