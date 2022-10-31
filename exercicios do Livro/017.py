'''Considerando 3 numeros inteiros digitados pelo usuario, exibi-los em ordem crescente'''
n1 = int(input())
n2 = int(input())
n3 = int(input())
aux = 0
while True:
    if n1 > n2:
        aux = n2
        n2 = n1
        n1 = aux
    if n2 > n3:
        aux = n3
        n3 = n2
        n2 = aux
    else:
        break
print(n1, n2, n3)