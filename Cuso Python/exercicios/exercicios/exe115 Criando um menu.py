def menu (msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-' *tam)
    print()
    print('\033[33m1 - \033[m\033[36mVer pessoas cadastradas\033[m')
    print('\033[33m2 - \033[m\033[36mCadastrar nova pessoa\033[m')
    print('\033[33m3 - \033[m\033[36mSair do Sistema\033[m')
    print('-'*30)

menu('MENU DE OPÇÕES')

while True:
    try:
        resp = int(input('\033[33mSua Opção:\033[m'))
    except (ValueError, TypeError):
        print('\033[31mErro\033[m')
        continue
    else:
        menu(f'{resp} sua opçao')

