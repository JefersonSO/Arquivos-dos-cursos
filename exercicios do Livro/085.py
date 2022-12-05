'''Utilizando  a agenda, escrever uma rotina que mostre a quantidade de
 pessoas cadastradas na agenda que possuem o DDD igual a 11'''

class Pessoa:
    _nome = ''
    _endereco = ''
    _ddd = ''
    _telefone = ''

    def _init_(self):
        self.nome = ""
        self.endereco = ""
        self.telefone = ""
        self.ddd = ''

    def set_nome (self, nome):
        self.nome = nome

    def get_nome(self):
        return(self.nome)

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_endereco(self):
        return(self.endereco)

    def set_ddd(self, ddd):
        self.ddd = ddd

    def get_ddd(self):
        return(self.ddd)

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_telefone(self):
        return(self.telefone)

agenda = list()
for c in range(0, 4):
    agenda.append(Pessoa())
i = 0


while i < len(agenda):
    agenda[i].set_nome(input('Digite o nome: '))
    agenda[i].set_endereco(input('Digite o endereço: '))
    agenda[i].set_ddd(input('DDD: '))
    agenda[i].set_telefone(input('Digite o telefone: '))


    i += 1



ddd11 = 0
i = 0
while i < len(agenda):
    print('-' * 32)
    print(f'Pessoa {i + 1}')
    print('-'*32)
    print('nome: ' + agenda[i].get_nome())
    print('Endereço: ' + agenda[i].get_endereco())
    print('DDD: ' + agenda[i].get_ddd())
    print('Telefone: ' + agenda[i].get_telefone())
    if '11' in agenda[i].ddd:
        ddd11 += 1
    i += 1

print(f'O total de pessoas com o DDD 11 é {ddd11}')
