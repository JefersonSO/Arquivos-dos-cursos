nome = str(input('Digite o seu nome completo: ')).strip()
Ma = nome.upper()
Me = nome.lower()
re = nome.split()
quantt = len(nome) - nome.count(' ')
print(' Em maiusculo: {} \n Em minuscula: {} \n Quantidade de letras: {} '.format(Ma, Me, quantt))
print(' Quantidade de letras no primeiro nome: {} '.format(nome.find(' ')))

