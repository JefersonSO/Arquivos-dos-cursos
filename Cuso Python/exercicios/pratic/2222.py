expr = str(input('digite uma expressao: '))
pilha = []
for simb in expr:
    if simb in '(':
        pilha.append('(')
    elif simb == '(':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
     print(' Essa é uma expressão válida.')
else:
    print(' Essa não é uma expressão válida.')




































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































