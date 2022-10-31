def linha(msg):
    print('-'*35)
    print(msg)
    print('-'*35)

def area(a, b):
    r = a * b
    print(f'A area de um terreno {a}x{b} é de {r}m')

#programa principal
linha('CONTROLE DE TERRENOS')

larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(larg, comp)
