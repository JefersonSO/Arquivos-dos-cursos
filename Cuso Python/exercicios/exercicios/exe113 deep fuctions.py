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


def leiaFloat(a):
    while True:
        try:
            n2 = float(input(a))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero real valido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuaro preferiu nao digitar esse numero\033[m')
            return 0
        else:
            return n2


n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o numero real foi {n2}')