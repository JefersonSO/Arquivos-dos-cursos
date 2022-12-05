'''Definir uma estrutura que permita armazenar o nome e as notas de alunos
de uma turma com 10 alunos, na qual, cada aluno possui duas nptas.
Em seguida, o programa deverà calcular e exibir o nome, a media
final de cada um dos alunos indicando, caso  a media seja menor
que 6,0  que o aluno esta reprovado, caso contrario, deveremos
mostrar que o aluno esta aprovado'''

class Alunos:
    _nome = ''
    _n1 = 0
    _n2 = 0
    _media = 0

    def _init_(self):
        self.nome = ''
        self.n1 = 0
        self.n2 = 0
        self.media = 0

    def set_nome(self,nome):
        self.nome = nome

    def get_nome(self):
        return(self.nome)

    def set_n1(self, n1):
        self.n1 = n1

    def get_n1(self):
        return (self.n1)

    def set_n2(self,n2):
        self.n2 = n2

    def get_n2(self):
        return(self.n2)

    def set_media(self, media):
        self.media = media

    def get_media(self):
        return(self.media)

i = 0
Os_Alunos = list()
for c in range(0,2):
    Os_Alunos.append(Alunos())

while i < len(Os_Alunos):
     Os_Alunos[i].set_nome(input('Nome: '))
     Os_Alunos[i].set_n1(float(input('1º nota: ')))
     Os_Alunos[i].set_n2(float(input('2º nota: ')))
     Os_Alunos[i].set_media(float((Os_Alunos[i].get_n1() + Os_Alunos[i].get_n2()) / 2))
     i += 1

i = 0
print('-' * 32)
while i < len(Os_Alunos):
        print(f'{i+1}º Aluno: ')
        print(f'1º nota: {Os_Alunos[i].get_n1()}')
        print(f'2º nota: {Os_Alunos[i].get_n2()}')
        print(f'A sua media é:{(Os_Alunos[i].get_media())}')

        if Os_Alunos[i].media > 6:
            print('-'*32)
            print('Aluno aprovado!')
            print('-' * 32)
        else:
            print('-' * 32)
            print('Aluno reprovado.')
            print('-' * 32)

        i += 1
