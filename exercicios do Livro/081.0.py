class Pessoa:
    _nome = ''
    _endereco = ''
    _telefone = ''

    def _init_(self):
        self.nome = ""
        self.endereco = ""
        self.telefone = ""

    def set_nome (self, nome):
        self.nome = nome

    def get_nome(self):
        return(self.nome)

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_endereco(self):
        return(self.endereco)

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_telefone(self):
        return(self.telefone)

agenda = [Pessoa(), Pessoa(), Pessoa()]
i = 0
while i < len(agenda):
    agenda[i].set_nome(input('Digite o nome: '))
    agenda[i].set_endereco(input('Digite o endereço: '))
    agenda[i].set_telefone(input('Digite o telefone: '))
    i += 1

i = 0
while (i < len(agenda)):
    print('-' * 32)
    print(f'Pessoa {i + 1}')
    print('-'*32)
    print('nome: ' + agenda[i].get_nome())
    print('Endereço: ' + agenda[i].get_endereco())
    print('Telefone: ' + agenda[i].get_telefone())
    i += 1

