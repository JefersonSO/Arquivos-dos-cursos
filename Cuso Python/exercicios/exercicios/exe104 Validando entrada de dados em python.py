def leiaInt(a):
    ok = True
    valor = 0
    while True:
        n = str(input(a))
        if n.isnumeric():
           valor = int(n)
           ok = True
        else:
            print('Erro')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'O valor digitado foi {n}')