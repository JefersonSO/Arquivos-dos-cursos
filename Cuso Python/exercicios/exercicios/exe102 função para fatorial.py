def fatorial(n, show=False):
    print('-'*30)
    cont = n
    f = 1

    while True:
        if show:
           print(f' {cont} x ', end='')
        f *= cont
        cont -= 1
        if cont == 0:
            break
    print(f' ={f}')
    return f


fatorial(5, show=True)