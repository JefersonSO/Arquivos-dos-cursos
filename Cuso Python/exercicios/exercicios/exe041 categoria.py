from datetime import date
nas = int(input('Digite a sua data de nascimento: '))
idade = date.today().year - nas
print('Você tem {} anos '.format(idade))
if idade <= 9:
    print('Sua categoria é \033[0;34mMIRIM')
elif idade <= 14:
    print('Sua categoria é \033[0;34mINFANTIL')
elif idade <= 19:
    print('Sua categoria é \033[0;34mJÚNIOR')
elif idade <= 25:
    print('Sua categoria é \033[0;34mSÊNIOR')
else:
    print('Sua categoria é \033[0;34mMASTER')
