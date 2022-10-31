from utilidadesCeV.exe104 import moeda

n = float(input('Digite um preço R$: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10% temos, {moeda.moeda(moeda.aumentando(n, 10))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(n, 13))}')