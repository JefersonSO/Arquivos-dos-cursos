re = 'Ss'
cont = soma = media = maior = menor = 0
while re in 'Ss':
    n = int(input('Digite um numero: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    re = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / cont
print('Voce digitou {} numero(s) e a media foi {} o maior foi {} e o menor foi {} '.format(cont, media, maior, menor))
print('fim.')