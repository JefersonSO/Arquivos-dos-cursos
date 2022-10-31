'''A partir de 5 letras digitadas pelo usuario, determinar e mostra quantas são vogais'''
print('Digite 5 letras: ')
l1 = str(input())
l2 = str(input())
l3 = str(input())
l4 = str(input())
l5 = str(input())
quantV = 0
if l1 in 'aeiou':
    quantV += 1
if l2 in 'aeiou':
    quantV += 1
if l3 in 'aeiou':
    quantV += 1
if l4 in 'aeiou':
    quantV += 1
if l5 in 'aeiou':
    quantV += 1

print(f'Das letras digitadas ao todo {quantV} são vogais')
