'''Utilizando  a agenda, elaborar uma rotina que, a partir de um nome
 digitado pelo usuario, mostre o DDD e o telefone da pessoa. '''

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

print('-'*23)
usuario = str(input('Digite um nome de usuario: '))


i = 0
while i < len(agenda):
    if agenda[i].nome == usuario:
        print('-' * 32)
        print(f'Pessoa {i + 1}')
        print('-'*32)
        print('DDD: ' + agenda[i].get_ddd())
        print('Telefone: ' + agenda[i].get_telefone())
    i += 1



