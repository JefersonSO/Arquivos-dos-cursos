'''Desenvolver uma rotina que apartir de 10 letras digitadas pelo usuario,
determine e mostre a qunatidade de vogais e tambem a quantidade de consoantes.'''
vogais = 0
consoantes = 0
for l in range(1,11):
    letra = str(input('Digite uma letra: ')).upper()
    if letra in 'AEIOU':
        vogais += 1
    else:
        consoantes += 1

print(f'Das letras digitadas {vogais} são vogais e {consoantes} são consoantes.')