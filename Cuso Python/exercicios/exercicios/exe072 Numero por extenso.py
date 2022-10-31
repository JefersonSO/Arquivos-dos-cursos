valores = ('zero', 'Um', 'dois', 'Tres', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'catorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
     n = int(input('Digite um numero de 0 a 20: '))
     if 0 <= n <= 20:
         break
print(valores[n])