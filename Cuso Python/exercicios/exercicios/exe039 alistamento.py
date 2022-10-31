from datetime import date
atual = date.today().year
nasc = int(input('Qual a sua idade: '))
idade = atual - nasc
print('Você nasceu em {} e tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce deve se alistar nesse ano')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento. '.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveia ter se alistado á {} anos.'.format(saldo))
    ano = atual - saldo
    print('O ano do seu alistamento foi {}'.format(ano))

