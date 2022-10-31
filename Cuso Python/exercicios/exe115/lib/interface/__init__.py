def leiaInt(a):
    while True:
        try:
            n1 = int(input(a))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuaro preferiu nao digitar esse numero\033[m')
            return 0
        else:
            return n1


def linha(tam=42):
    return '-' *tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[36m{item}\033[m ')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
