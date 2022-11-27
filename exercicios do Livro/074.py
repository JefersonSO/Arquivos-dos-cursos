from random import randint

'''Desenvolver um algoritmo que efetue a leitura de dez numeros e os
armazene em uma lista "A".' Em seguida a lista "B" do mesmo tipode dado,
deverá ser carregado observando a seguinte regra: se o indice for par,
o valor do elemento devera ser multiplicado por 5, caso contrario,
deverá ser somado com 5. Ao final, o programa deverá mostrar os valores
armazenados nos dois vetores. '''



A = list()
B = list()
par = 0
for c in range(0,10):
    num = randint(0,10)
    A.append(num)
    if num % 2 == 0:
        B.append(num*5)
    else:
        B.append(num+5)

print('A =',end=' ')
for n in A:
    print(n,end='  ')
print()
print('B =',end=' ')
for n in B:
    print(n,end=' ')