s = float(input('\033[1;33mDigite o salario : '))
c = s+(s*30/100)
print(' Salario atual  R$ {}{}{} \n \033[1;33msalario com aumento de \033[1;36m15%\033[m  \033[1;33mR$ {}{:.2f}{}' .format('\033[1;32m', s,'\033[m', '\033[1;32m', c, '\033[1;32m'))