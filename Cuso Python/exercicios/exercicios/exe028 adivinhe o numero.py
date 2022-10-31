from random import randint
print('Vou escolher um numero de 0 a 5')
c = randint(0, 5)
q = int(input('consegue adivinhar?'))
if q == c:
    print('O numero que eu escolhi {} Parabéns você venceu!'.format(c))
else:
    print('O numero que eu escolhi {}  você perdeu.'.format(c))
