km = float(input('Quantos km é a sua viagem? '))
if km>200:
    print('A passgem custa {:.2f} '.format(km*0.45))
else:
    print('A passagem custa {:.2f}' .format(km*0.50))