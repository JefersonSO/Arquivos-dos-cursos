'''Acrescentar ao exemplo da calculadora simples um procedimento para
calcular o quadrado de um numero real digitado pelo usuario.'''



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

def potencia(n1):
    s = n1 * n1
    print(f'{n1}² = {s}')



print('-'*25)
print('Calculadora simples')
print('-'*25)

while True:
     simb = int(input('1 [+] \n2 [-] \n3 [x] \n4 [/] 5 [**]'))
     if simb == 5:
         v1 = float(input('nº: '))
     else:
         v1 = int(input('nº: '))
         v2 = int(input('nº: '))
     if simb == 1:
         somar(v1,v2)
     elif simb == 2:
         subtrair(v1,v2)
     elif simb == 3:
         multiplicar(v1,v2)
     elif simb == 4:
         dividir(v1,v2)
     elif simb == 5:
         potencia(v1)


     r = str(input('Continuar [S / N]')).upper()
     if 'N' in r:
         print('Fim.')
         break