'''Considerando seis numeros inteiros representando dois intervalos
 de tempo (horas, minutos e segundos), elaborar uma rotina que calcule a diferença de tempo entre os intervalos. '''

hora = int(input('Digite a hora: '))
min = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
print(f'{hora}:{min}:{segundos}  ')
print(f'A diferença entre a hora e os minutos é de {60-min} minutos e a diferebça entre os minutos'
      f'e os segundos é {60-segundos}segundos')