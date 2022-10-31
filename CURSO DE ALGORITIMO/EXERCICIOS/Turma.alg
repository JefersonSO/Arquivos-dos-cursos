algoritmo "Turma"

var
nome: Vetor[1..4] de Caractere
n1: Vetor[1..4] de Real
n2: Vetor[1..4] de Real
media: Vetor [1..4] de Real
SM, MT: Real
C, tot : Inteiro
inicio
Para C <- 1 ate 4 faca
   Escreva(" Nome: ")
   Leia(nome[C])
   Escreva(" Primeira nota: ")
   Leia(n1[C])
   Escreva(" Segunda nota: ")
   Leia(n2[C])
   media[C] <-(n1[C]+ n2[C]) / 2
   SM <- SM + media[C]
   
FimPara
MT <- SM / 4
LimpaTela
Escreval("--------------------")
Escreval(" Media dos Alunos ")
Escreva("--------------------")
Para C <- 1 ate 4 faca
   Escreval(nome[C]:15, media[C])
   Se (media[C] > MT) entao
      tot <- tot + 1
FimPara
fimalgoritmo
