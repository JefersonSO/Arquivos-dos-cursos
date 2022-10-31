notas = list()
media = aluno = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    notas.append([nome, nota1, nota2, media])
    r = str(input('Continuar? S/N'))
    if r in'Nn':
        break
print('-='* 35)
print('Nº. NOME       MÈDIA')
print('-'*35)

for a, n in enumerate(notas):
    print(f'{a:<4}{n[0]:<10}{n[3]:>8.1f}')
print()
print('-'*35)
while True:
    mostrar = int(input('Mostrar as notas de qual aluno? (999intenrrompe)'))
    if mostrar == 999:
        print('fim')
        break
    else:
        print(f'Notas de {notas[mostrar][0]} são {notas[mostrar][1]} {notas[mostrar][2]}')
    print('-'*35)


