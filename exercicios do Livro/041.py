'''A partir se uma temperatura e opção de conversão, fornecidas pelo usuario,
realize a conversão entre as temperaturas conforme ilustrado pela tabelaa seguir.
Após cada conversão o programa deverá perguntar se o usuario desejarealizar uma
nova conversão. Quando o usuario digitar "sim" uma nova temperaturae opção de
conversão deverão  ser solicitadas, caso contrario, o programa deverá ser encerrado.
tabela:

             DE           PARA          FORMULA
      ----------------------------------------------------
       Celsius       Fahrenheit    ºF = ºC x 1,8 + 32
       Fahrenheit    Celsius       ºC = (ºF - 32) / 1,8
       Celsius       Kelvin        K = ºC+ 273,15
       Kelvin        Celsius       ºC = K - 273,15
       Fahrenheit    Kelvin        K =(ºF + 459,67) / 1,8
       Kelvin        Fahrenheit    ºF = K x 1,8 - 459,67
      ---------------------------------------------------- '''

while True:
    temp = float(input('Digite a temperatura: '))
    print('Escolha as opções de conversão Celsius [C]  Fahrenheit [F] Kelvin [K]')
    esc1 = str(input('Converter De: ')).upper()
    esc2 = str(input('Para: ')).upper()
    if esc1 in 'C' and esc2 in 'F':
        print(f'ºC{temp}  = ºF {(temp*1.8) + 32}')

    elif esc1 in 'F' and esc2 in 'C':
          print(f'ºF {temp} = ºC {(temp-32) / 1.8}')

    elif esc1 in 'C' and esc2 in 'K':
          print(f'ºC {temp} = K {temp + 273.15}')

    elif esc1 in 'K' and esc2 in 'C':
        print(f'K {temp} = ºC {temp - 273.15}')

    elif esc1 in 'F' and esc2 in 'K':
        print(f'ºF {temp} = K {(temp + 459.67) / 1.8}')

    elif esc1 in 'K' and esc2 in 'F':
        print(f'K {temp} = ºF {temp * 1.8 - 459.67}')
    else:
        print('Escolha uma pção valida.')

    esc3 = str(input('Fazer uma nova conversão? [S]/[N]')).upper()
    if esc3 in 'N':
        print('fim.')
        break
