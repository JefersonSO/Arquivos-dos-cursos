n = int(input('\033[1;34mDigite um numero: \033[m'))
print('{}O antecessor de {} é {}{}{} {}e seu sucessor é {}{}{}.' .format('\033[1;34m', n,'\033[4;34m', n-1, '\033[m',
           '\033[1;34m', '\033[4;34m', n+1, '\033[1;34m' ))

