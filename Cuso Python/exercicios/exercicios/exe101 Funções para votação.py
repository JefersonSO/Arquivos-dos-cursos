

def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - anonsc
    print('-='*30)
    if idade < 16:
        return F'Com {idade} anos : NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos : VOTO OPCIONAL.'
    elif idade >= 18 and idade < 60:
        return f'Com {idade} anos : VOTO OBRIGATORIO. '

anonsc = int(input('Em que ano você nasceu?: '))
print(voto(anonsc))