lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Continuar ? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'os digitados em ordem decrescente {lista}')
if 5 in lista:
   print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado')