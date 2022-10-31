numero = int(input('Primeiro numero'))
numero2 = int(input('Segundo numero'))
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{} !'.format('\033[1;31m', numero, '\033[m', '\033[1;31m', numero2, '\033[m', '\033[4;32m',  numero+numero2, '\033[m'))