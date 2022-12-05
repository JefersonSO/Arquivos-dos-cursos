'''Criar u programa que, a partir de uma relação de 100 veiculos contendo
modelo, ano de fabricação e cor, exibir quantos são da cor azul.'''

class carros:
    _modelo = ''
    _fabriccao = ''
    _cor = ''

    def _init_(self):
        self.modelo = ''
        self.fabricacao = ''
        self.cor = ''

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return(self.modelo)

    def set_fabricacao(self, fabricacao):
        self.fabricacao = fabricacao

    def get_fabricacao(self):
        return(self.fabricacao)

    def set_cor(self, cor):
        self.cor = cor

    def get_cor(self):
        return(self.cor)


todos = list()
for c in range(0,101):
    todos.append(carros())

i = 0
azuis = 0

while i < len(todos):
    todos[i].set_modelo(input('Modelo: '))
    todos[i].set_fabricacao(input('Fabricação: '))
    todos[i].set_cor(input('Cor: ').upper())
    i += 1
i = 0
while i < len(todos):
    if 'AZUL' in todos[i].cor:
        azuis += 1
    i += 1
print(f'Dos veiculos citados {azuis} são da cor azul.')