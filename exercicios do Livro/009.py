''' Calcular o IMC de uma pessoa e mostrar a condição em que ela esta. '''

altura = (float(input('Altura m: ')))
peso = (float(input('peso kg:')))
imc = peso / (altura**2)
print('------Valor do IMC-----------Situação-----------')
print('''  Abaixo 18.5           a baixo do peso ideal 
  entre 18,5 e 24,9       peso normal          
  entre 25,0 e 29,9       acima do peso ideal  
  entre 30,3 e 34,9       obesidade grau I   
  entre 35,0 e 39,9       obesidade grau II  
  entre 40,0 e acima      obesidade grau III''')
print('-'*45)
print(f'Seu IMC é: {imc:.2f}')
if imc < 18.5:
    print('Você esta abaixo do peso ideal ')
elif imc >= 18.5 and imc <= 24.9:
    print('Parabens, voce esta no seu peso normal!')
elif imc >= 25.0 and imc <= 29.9:
    print('Você esta acima do seu peso(sobrepeso)')
elif imc >= 30.0  and imc <= 34.9:
    print('Obesidade grau I')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade grau II')
elif imc >= 40:
    print('Obesidade grau III')


