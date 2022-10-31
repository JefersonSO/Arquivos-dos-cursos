soma = 0
maior = 0
menor = 0
mvelho = 0
totmulher = 0
for n in range(1, 5):
    nome = str(input(' qual o nome da {}º pessoa : '.format(n)))
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo F/ M: '.upper()))
    soma += idade
    if idade == 1 and sexo in 'Mm':
        maior = idade
        mvelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        mvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = soma / 4
print('A media de idade é: {}'.format(media))
print('O home com a maior idade tem {} e se chama {}'.format(maior, mvelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher))



