frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inversão = ''
for letra in range(len(junto) - 1, -1, -1):
    inversão += junto[letra]
print('O iverso de {} é {}'.format(junto, inversão))
if inversão == junto:
    print('Temos um PALINDROMO')
else:
    print('A frase digitada não é um palindromo')


