f = 'feminino'
m = 'masculino'
n = str(input('Digite o seu sexo [F/M] ')).upper
while n != 'F' and n != 'M':
    n = str(input('valor Invalido, digite novamente ')).upper()
    if n == 'F':
        print('Ok voce é do sexo {} . '.format(f))
    if n == 'M':
        print('Ok voce é do sexo {} . '.format(m))

print('fim.')



