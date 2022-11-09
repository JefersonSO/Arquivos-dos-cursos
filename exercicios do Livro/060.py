'''Elaborar um programa que apartir de uma determinada quantidade de
linhas e colunas digitadas pelo usuario exiba um retangulo, por exemplo:

Entrada:
Linhas ? 4
Colunas ? 6

Saida:
+----+
│    │
│    │
+----+       '''

l = int(input('Linhas: '))
c = int(input('Colunas: '))
for cont in range(1, l+1):
    if cont == 1:
        print(f'+{"-"*(c-2)}+')
    if cont >1 and cont < l:
        print(f'│{" " * (c - 2)}│')
    if cont == l:
        print(f'+{"-" * (c - 2)}+')