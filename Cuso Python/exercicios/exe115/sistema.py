from exe115.lib.interface import *
from exe115.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...até logo!')
        break
    else:
        print('\033[31mERRO! Digite um numero valido!\033[m')
    sleep(2)