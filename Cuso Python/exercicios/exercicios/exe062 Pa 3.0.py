primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -'.format(termo), end='')
        cont += 1
        termo += razão
    print('pausa')
    mais = int(input('Quantos termos quer mostrar:'))
print('fim.')