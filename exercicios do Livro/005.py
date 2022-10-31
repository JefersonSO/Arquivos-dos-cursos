'''Calcular a média de duas notas de um aluno e determinar que,
pra ser aprovado a media deve ser no minimo  6, mostra se o aluno foi ou não aprovado. '''

n1 = float(input())
n2 = float(input())
media = (n1+n2) / 2
if media >= 6:
    print(f'A media foi {media}. Aluno aprovado!')
else:
    print(f'A media é {media}. Aluno reprovado.')
