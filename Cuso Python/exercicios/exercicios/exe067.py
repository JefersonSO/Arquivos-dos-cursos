while True:
    print('-'*20)
    n = int(input('Qual a tabuada?:'))
    print('-'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {c * n}')

print('fim do progama.')
