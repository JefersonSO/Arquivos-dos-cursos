def metade(num=0, f=False ):
    res = num / 2
    return res if f is False else moeda(res)


def dobro(num=0, f=False):
    res = num * 2
    return res if f is False else moeda(res)


def aumentando(num=0, taxa=0, f=False):
    res = num + (num * taxa) / 100
    return res if not f else moeda(res)


def diminuir(num=0, taxa=0, f=False):
    res = num - (num * taxa) / 100
    return res if f is False else moeda(res)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:>8.2f}'.replace('.',',')

def resumo(num=0, taxa=0, taxa2=0):
    msg = ('  Resumo do Valor ')
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)} ')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{taxa}% de aumento: \t{aumentando(num, taxa, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(num, taxa, True)}')
    print('-' * tam)

