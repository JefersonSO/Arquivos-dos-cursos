n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
m = (n1 + n2) / 2
print('Media {}'.format(m))
if m < 5.0:
    print('Media abaixo de 5.0: \033[0;31mREPROVADO')
elif m == 5.0 or m <= 6.9:
    print('Media entre 5.0 e 6.9: \033[0;34mRECUPERAÇÃO')
elif m >=7:
    print('Media superior a 7.0: \033[0;32mAPROVADO!')