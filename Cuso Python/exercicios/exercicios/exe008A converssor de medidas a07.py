m = float(input('Digite o metro'))
print('\033[32m', '-='*20)
km = m / 1000
hm = m / 100
dam =m / 10
m = m
dm = m * 10
cm = m * 100
mm = m * 1000
print(' Kilômetro = {}km \n Hequiômetro = {}hm \n Decâmetro = {} dam \n Metro = {}m \n Decímetro {}dm'.format(km, m, hm, dam, m, dm))
print(' Centímetro {}cm \n milímetro {}mm'.format(cm, mm))
print('\033[32m', '-='*20)