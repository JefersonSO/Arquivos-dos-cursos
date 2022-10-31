exp = str(input('Digite a expressão: '))
temp = []
for s in exp:
    if s == '(':
        temp.append('(')
    elif s == ')':
         if len(temp) > 0:
            temp.pop()
         else:
             temp.append(')')
             break
if len(temp)== 0:
   print('Essa expressão é valida')
else:
   print('Expressão invalida')
