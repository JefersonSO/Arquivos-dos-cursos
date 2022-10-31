cont = m = f = 0
while True:
    print('-' * 22)
    print('CADASTRE UMA PESSOA')
    print('-' * 22)
    idade = int(input('Idade: '))
    sexo = c = ' '
    while sexo not in 'FM':
     sexo = str(input('Sexo: [M/F] ').upper().strip()[0])
    print('-' * 22)
    while c not in 'SN':
      c = str(input('Quer continuar? [S/N]').upper().strip()[0])
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
          f += 1
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {m} homens cadastrados e temos {f} mulher com menos de 20 anos cadastrados')
