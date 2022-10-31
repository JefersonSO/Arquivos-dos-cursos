'''A partir do salario e categoria, digitados pelo usuario , calcular o reajuste de salario de determinado
funcionario baseando-se na tabela mostrad a seguir, sendo que o programa devera aceitar tanto letras
maiusculas quanto minusculas para determinar a categoria do funcionario.

       REAJUSTE         CATEGORIA
       --------------------------
       10%              A,C
       15%              B,D,E
       25%              F,L
       35%              G,H
       50%              I,J
       --------------------------'''

salario = float(input('salario R$: '))
categoria = str(input('escolha a categoria A/B/C/D/E/F/L/G/H/I/J')).upper()
if categoria in 'A,C':
    print(f'Salario de R$ {salario} com reajuste {salario+salario*10/100}')
elif categoria in 'B,D,E':
    print(f'Salario de R$ {salario} com reajuste {salario+salario*15/100}')
elif categoria in 'F,L':
    print(f'Salario de R$ {salario} com reajuste {salario+salario*25/100}')
elif categoria in 'G,H':
    print(f'Salario de R$ {salario} com reajuste {salario+salario*35/100}')
elif categoria in 'I,J':
    print(f'Salario de R$ {salario} com reajuste {salario+(salario*50/100)}')
else:
    print('Valor invalido')


