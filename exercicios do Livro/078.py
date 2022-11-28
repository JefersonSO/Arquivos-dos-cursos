'''Com função, desenvolver uma calculadora simples '''

def somar(n1,n2):
    s = n1 + n2
    print(f'{n1} + {n2} = {s}')

def subtrair(n1,n2):
    s = n1 - n2
    print(f'{n1} - {n2} = {s}')

def multiplicar(n1,n2):
    s = n1 * n2
    print(f'{n1} x {n2} = {s}')

def dividir(n1,n2):
    s = n1 / n2
    print(f'{n1} / {n2} = {s}')

print('-'*25)
print('Calculadora simples')
print('-'*25)

while True:
     v1 = int(input('nº: '))
     simb = int(input('1 [+] \n2 [-] \n3 [x] \n4 [/] '))
     v2 = int(input('nº: '))
     if simb == 1:
         somar(v1,v2)
     elif simb == 2:
         subtrair(v1,v2)
     elif simb == 3:
         multiplicar(v1,v2)
     elif simb == 4:
         dividir(v1,v2)

     r = str(input('Continuar [S / N]')).upper()
     if 'N' in r:
         print('Fim.')
         break